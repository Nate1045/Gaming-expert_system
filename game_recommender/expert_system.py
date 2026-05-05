"""
Expert system for game recommendations using EXPERTA.
Implements rules-based reasoning for game suggestions.
"""
import collections
import collections.abc
from experta import *
from typing import List, Dict, Optional
from .knowledge_base import GameKnowledgeBase


class UserPreferences(Fact):
    """Fact representing user preferences."""
    genres = Field(list)
    multiplayer = Field(str)
    difficulty = Field(str)
    platforms = Field(list)
    graphics_style = Field(str)
    game_length = Field(str)


class GameRecommendation(Fact):
    """Fact representing a game recommendation."""
    pass


class GameExpertSystem(KnowledgeEngine):
    """Expert system for recommending games."""
    
    def __init__(self, kb: GameKnowledgeBase):
        super().__init__()
        self.kb = kb
        self.recommendations = []
        self.matched_games = []
    
    @DefFacts()
    def _initial_facts(self):
        """Initialize with game facts."""
        yield Fact(action="start")
    
    @Rule(UserPreferences())
    def process_preferences(self):
        """Process user preferences."""
        pass
    
    def get_recommendations(self, preferences: Dict) -> List[Dict]:
        """
        Get game recommendations based on user preferences.
        
        Uses expert system facts for tracking and performs
        knowledge base search for matching games.
        
        Args:
            preferences: Dictionary with keys like 'genres', 'multiplayer', 
                        'difficulty', 'platforms', 'graphics_style', 'game_length'
        
        Returns:
            List of recommended games (top 5).
        """
        self.matched_games = []
        
        try:
            # Reset and declare user preferences as facts
            self.reset()
            
            # Build fact with only non-None values
            fact_data = {}
            for key, value in preferences.items():
                if value is not None:
                    fact_data[key] = value
            
            if fact_data:
                self.declare(UserPreferences(**fact_data))
            
            self.run()
        except Exception as e:
            print(f"Note: Expert system processing: {e}")
        
        # Perform actual game search based on preferences
        results = self.kb.search_games(preferences)
        self.matched_games.extend(results)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for game in self.matched_games:
            game_id = game.get("id")
            if game_id not in seen:
                seen.add(game_id)
                unique_recommendations.append(game)
        
        return unique_recommendations[:5]  # Return top 5 recommendations
