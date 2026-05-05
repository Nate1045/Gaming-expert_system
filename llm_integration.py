"""
LLM integration for fallback game recommendations.
Handles communication with OpenRouter API (free tier).
"""

import os
from typing import Dict, Optional, List
import json
import requests


class LLMIntegration:
    """Integrates with OpenRouter for hybrid recommendations."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize LLM integration with OpenRouter."""
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if self.api_key:
            print(f"✓ OpenRouter API key detected: {self.api_key[:10]}...")
        else:
            print("ℹ️  OPENROUTER_API_KEY not set. LLM features disabled.")
            print("   Get a free API key at: https://openrouter.ai/keys")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/your-repo/expert-system",
            "X-Title": "Game Recommendation Expert System"
        }
    
    def recommend_game(self, preferences: Dict, exclude_games: List[str] = None) -> Optional[str]:
        """
        Use Hugging Face LLM to recommend a game based on preferences.
        """
        if not self.api_key:
            return None
        
        prompt = self._build_recommendation_prompt(preferences, exclude_games)
        response_text = self._query_model(prompt, temperature=0.7, max_tokens=300)
        return response_text
    
    def extract_game_info(self, game_name: str) -> Optional[Dict]:
        """
        Use Hugging Face LLM to extract detailed game information.
        """
        if not self.api_key:
            return None
        
        prompt = (
            "You are a gaming database expert. Extract game information and respond in JSON format.\n\n"
            "Return a JSON object with these fields:\n"
            "- name: Game title\n"
            "- genres: Array of genres from [Action, RPG, Strategy, Puzzle, Adventure, Sports, Simulation, Horror]\n"
            "- multiplayer: One of [Single-player, Local Co-op, Online Multiplayer, Competitive]\n"
            "- difficulty: One of [Easy, Medium, Hard]\n"
            "- platforms: Array from [PC, PlayStation, Xbox, Nintendo Switch, Mobile]\n"
            "- graphics_style: One of [Realistic, Cartoon, Pixel Art, Anime]\n"
            "- game_length: One of [Short (< 10 hours), Medium (10-30 hours), Long (30+ hours)]\n"
            "- year: Release year (number)\n"
            "- description: Brief description\n\n"
            f"Extract information for the game: {game_name}"
        )
        response_text = self._query_model(prompt, temperature=0.3, max_tokens=300)
        if not response_text:
            return None
        
        try:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response_text[start:end])
        except json.JSONDecodeError:
            print("Failed to parse JSON from LLM response")
        return None
    
    def validate_game_data(self, game: Dict) -> bool:
        """Validate if game data has required fields."""
        required_fields = ["name", "genres", "multiplayer", "difficulty", 
                          "platforms", "graphics_style", "game_length"]
        return all(field in game for field in required_fields)
    
    def _build_recommendation_prompt(self, preferences: Dict, exclude_games: List[str]) -> str:
        """Build a prompt for LLM recommendation."""
        prompt = "Recommend a game based on these preferences:\n\n"
        for key, value in preferences.items():
            if value:
                prompt += f"- {key}: {value}\n"
        
        if exclude_games:
            prompt += f"\nPlease don't recommend: {', '.join(exclude_games)}\n"
        
        prompt += "\nProvide a game recommendation with a brief explanation of why it matches these preferences."
        return prompt
    
    def _query_model(self, prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Send prompt to OpenRouter API."""
        try:
            payload = {
                "model": "openrouter/owl-alpha",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "top_p": 0.9,
                "top_k": 40,
                "repetition_penalty": 1.1
            }
            response = requests.post(self.base_url, headers=self.headers, json=payload, timeout=30)
            
            # Handle rate limiting gracefully
            if response.status_code == 429:
                print("⚠️  LLM rate-limited. Using knowledge base only for now.")
                return None
            
            if response.status_code != 200:
                print(f"OpenRouter error {response.status_code}: {response.text}")
                return None

            data = response.json()
            if "choices" in data and data["choices"]:
                return data["choices"][0]["message"]["content"]
            return None
        except Exception as e:
            print(f"Error querying OpenRouter: {e}")
            return None
    
    def is_available(self) -> bool:
        """Check if the Hugging Face API key is available."""
        return bool(self.api_key)
