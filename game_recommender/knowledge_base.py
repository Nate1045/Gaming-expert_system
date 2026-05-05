"""
Knowledge base management for games.
Handles storage, retrieval, and updates to the game database.
"""

import json
import os
from typing import List, Dict, Optional
from datetime import datetime


class GameKnowledgeBase:
    """Manages the game knowledge base."""
    
    def __init__(self, db_file: str = "data/games.json"):
        self.db_file = db_file
        self.games = []
        self._ensure_data_dir()
        self._load_games()
        if not self.games:
            self._initialize_default_games()
    
    def _ensure_data_dir(self):
        """Ensure data directory exists."""
        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)
    
    def _load_games(self):
        """Load games from JSON file."""
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as f:
                    self.games = json.load(f)
            except json.JSONDecodeError:
                self.games = []
        else:
            self.games = []
    
    def _save_games(self):
        """Save games to JSON file."""
        with open(self.db_file, 'w') as f:
            json.dump(self.games, f, indent=2)
    
    def _initialize_default_games(self):
        """Initialize with default games."""
        default_games = [
            {
                "id": 1,
                "name": "The Legend of Zelda: Breath of the Wild",
                "genres": ["Adventure", "Action"],
                "multiplayer": "Single-player",
                "difficulty": "Medium",
                "platforms": ["Nintendo Switch"],
                "graphics_style": "Cartoon",
                "game_length": "Long (30+ hours)",
                "year": 2017,
                "description": "Open-world action-adventure game"
            },
            {
                "id": 2,
                "name": "Elden Ring",
                "genres": ["RPG", "Action"],
                "multiplayer": "Single-player",
                "difficulty": "Hard",
                "platforms": ["PC", "PlayStation", "Xbox"],
                "graphics_style": "Realistic",
                "game_length": "Long (30+ hours)",
                "year": 2022,
                "description": "Action RPG with challenging combat"
            },
            {
                "id": 3,
                "name": "Portal 2",
                "genres": ["Puzzle"],
                "multiplayer": "Single-player",
                "difficulty": "Medium",
                "platforms": ["PC", "PlayStation", "Xbox"],
                "graphics_style": "Realistic",
                "game_length": "Medium (10-30 hours)",
                "year": 2011,
                "description": "First-person puzzle game"
            },
            {
                "id": 4,
                "name": "Super Smash Bros. Ultimate",
                "genres": ["Sports", "Action"],
                "multiplayer": "Local Co-op",
                "difficulty": "Easy",
                "platforms": ["Nintendo Switch"],
                "graphics_style": "Cartoon",
                "game_length": "Long (30+ hours)",
                "year": 2018,
                "description": "Fighting game with multiplayer focus"
            },
            {
                "id": 5,
                "name": "Civilization VI",
                "genres": ["Strategy"],
                "multiplayer": "Online Multiplayer",
                "difficulty": "Hard",
                "platforms": ["PC", "PlayStation", "Xbox"],
                "graphics_style": "Cartoon",
                "game_length": "Long (30+ hours)",
                "year": 2016,
                "description": "Turn-based strategy and civilization building"
            },
            {
                "id": 6,
                "name": "Hades",
                "genres": ["Action", "RPG"],
                "multiplayer": "Single-player",
                "difficulty": "Hard",
                "platforms": ["PC", "Nintendo Switch", "PlayStation", "Xbox", "Mobile"],
                "graphics_style": "Pixel Art",
                "game_length": "Medium (10-30 hours)",
                "year": 2020,
                "description": "Roguelike dungeon crawler with dark theme"
            },
            {
                "id": 7,
                "name": "Stardew Valley",
                "genres": ["Simulation"],
                "multiplayer": "Single-player",
                "difficulty": "Easy",
                "platforms": ["PC", "Nintendo Switch", "Mobile", "PlayStation"],
                "graphics_style": "Pixel Art",
                "game_length": "Long (30+ hours)",
                "year": 2016,
                "description": "Farming and life simulation game"
            },
            {
                "id": 8,
                "name": "Among Us",
                "genres": ["Strategy"],
                "multiplayer": "Online Multiplayer",
                "difficulty": "Easy",
                "platforms": ["PC", "Mobile"],
                "graphics_style": "Cartoon",
                "game_length": "Short (< 10 hours)",
                "year": 2018,
                "description": "Social deduction party game"
            },
            {
                "id": 9,
                "name": "Resident Evil Village",
                "genres": ["Horror", "Action"],
                "multiplayer": "Single-player",
                "difficulty": "Hard",
                "platforms": ["PC", "PlayStation", "Xbox"],
                "graphics_style": "Realistic",
                "game_length": "Medium (10-30 hours)",
                "year": 2021,
                "description": "Survival horror game"
            },
            {
                "id": 10,
                "name": "Hollow Knight",
                "genres": ["Action", "Adventure"],
                "multiplayer": "Single-player",
                "difficulty": "Hard",
                "platforms": ["PC", "Nintendo Switch"],
                "graphics_style": "Pixel Art",
                "game_length": "Medium (10-30 hours)",
                "year": 2017,
                "description": "Metroidvania-style action-adventure"
            }
        ]
        self.games = default_games
        self._save_games()
    
    def get_all_games(self) -> List[Dict]:
        """Get all games from knowledge base."""
        return self.games
    
    def get_game_by_name(self, name: str) -> Optional[Dict]:
        """Get a game by its name (case-insensitive)."""
        name_lower = name.lower()
        for game in self.games:
            if game["name"].lower() == name_lower:
                return game
        return None
    
    def search_games(self, criteria: Dict) -> List[Dict]:
        """Search games based on criteria."""
        results = self.games.copy()
        
        # Filter by genres (if specified)
        if "genres" in criteria and criteria["genres"]:
            results = [
                game for game in results
                if any(g in game.get("genres", []) for g in criteria["genres"])
            ]
        
        # Filter by multiplayer type
        if "multiplayer" in criteria and criteria["multiplayer"]:
            results = [
                game for game in results
                if game.get("multiplayer") == criteria["multiplayer"]
            ]
        
        # Filter by difficulty
        if "difficulty" in criteria and criteria["difficulty"]:
            results = [
                game for game in results
                if game.get("difficulty") == criteria["difficulty"]
            ]
        
        # Filter by platform
        if "platforms" in criteria and criteria["platforms"]:
            results = [
                game for game in results
                if any(p in game.get("platforms", []) for p in criteria["platforms"])
            ]
        
        # Filter by graphics style
        if "graphics_style" in criteria and criteria["graphics_style"]:
            results = [
                game for game in results
                if game.get("graphics_style") == criteria["graphics_style"]
            ]
        
        # Filter by game length
        if "game_length" in criteria and criteria["game_length"]:
            results = [
                game for game in results
                if game.get("game_length") == criteria["game_length"]
            ]
        
        return results
    
    def add_game(self, game: Dict) -> bool:
        """Add a new game to the knowledge base."""
        # Check if game already exists
        if self.get_game_by_name(game.get("name", "")):
            return False
        
        # Assign new ID
        if self.games:
            game["id"] = max(g.get("id", 0) for g in self.games) + 1
        else:
            game["id"] = 1
        
        # Add timestamp
        game["added_date"] = datetime.now().isoformat()
        
        self.games.append(game)
        self._save_games()
        return True
    
    def update_game(self, game_id: int, updates: Dict) -> bool:
        """Update an existing game."""
        for game in self.games:
            if game.get("id") == game_id:
                game.update(updates)
                self._save_games()
                return True
        return False
    
    def delete_game(self, game_id: int) -> bool:
        """Delete a game from knowledge base."""
        for i, game in enumerate(self.games):
            if game.get("id") == game_id:
                self.games.pop(i)
                self._save_games()
                return True
        return False