"""
Expert system for game recommendations using EXPERTA.
Implements backward chaining for goal-directed reasoning.
"""
import collections
import collections.abc
from experta import KnowledgeEngine, Fact, Field, Rule, DefFacts, MATCH, AS
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
    game = Field(dict)


class Goal(Fact):
    """Goal fact for backward chaining."""
    name = Field(str)


class GameExpertSystem(KnowledgeEngine):
    """Expert system for recommending games using backward chaining."""
    
    def __init__(self, kb: GameKnowledgeBase):
        super().__init__()
        self.kb = kb
        self.recommendations = []
    
    @DefFacts()
    def _initial_facts(self):
        """Initialize with game facts."""
        yield Fact(action="start")
    
    @Rule(Goal(name='find_recommendation'))
    def find_recommendation(self):
        """Backward chaining rule to find recommendations when goal is set."""
        # Get user preferences from facts
        user_prefs = None
        for fact in self.facts.values():
            if isinstance(fact, UserPreferences):
                user_prefs = fact
                break
        
        if not user_prefs:
            return
        
        preferences = {}
        if 'genres' in user_prefs:
            preferences['genres'] = user_prefs['genres']
        if 'multiplayer' in user_prefs:
            preferences['multiplayer'] = user_prefs['multiplayer']
        if 'difficulty' in user_prefs:
            preferences['difficulty'] = user_prefs['difficulty']
        if 'platforms' in user_prefs:
            preferences['platforms'] = user_prefs['platforms']
        if 'graphics_style' in user_prefs:
            preferences['graphics_style'] = user_prefs['graphics_style']
        if 'game_length' in user_prefs:
            preferences['game_length'] = user_prefs['game_length']
        
        # Perform knowledge base search
        results = self.kb.search_games(preferences)
        
        # Declare recommendations as facts
        for game in results[:5]:  # Limit to top 5
            self.declare(GameRecommendation(game=game))
    
    def get_recommendations(self, preferences: Dict) -> List[Dict]:
        """
        Get game recommendations using backward chaining.
        
        Declares a goal to find recommendations and lets the expert system
        work backwards from the goal to find matching games.
        
        Args:
            preferences: Dictionary with keys like 'genres', 'multiplayer', 
                        'difficulty', 'platforms', 'graphics_style', 'game_length'
        
        Returns:
            List of recommended games (top 5).
        """
        self.recommendations = []
        
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
            
            # Declare the goal to find recommendations (backward chaining trigger)
            self.declare(Goal(name='find_recommendation'))
            
            # Run the expert system (backward chaining via goal)
            self.run()
            
            # Collect recommendations from facts
            for fact in self.facts.values():
                if isinstance(fact, GameRecommendation):
                    self.recommendations.append(fact['game'])
                    
        except Exception as e:
            print(f"Note: Expert system processing: {e}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for game in self.recommendations:
            game_id = game.get("id")
            if game_id not in seen:
                seen.add(game_id)
                unique_recommendations.append(game)
        
        return unique_recommendations[:5]  # Return top 5 recommendations
