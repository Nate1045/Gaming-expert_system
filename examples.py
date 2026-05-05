"""
Example usage of the expert system without GUI.
Shows how to use the components programmatically.
"""

from game_recommender.knowledge_base import GameKnowledgeBase
from game_recommender.expert_system import GameExpertSystem
from game_recommender.llm_integration import LLMIntegration
from game_recommender import config
import json


def example_basic_search():
    """Example: Basic game search."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Game Search")
    print("="*60)
    
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    
    # Search for action games
    criteria = {"genres": ["Action"]}
    results = kb.search_games(criteria)
    
    print(f"\nFound {len(results)} action games:")
    for game in results:
        print(f"  - {game['name']} ({game['year']})")


def example_expert_system():
    """Example: Get expert system recommendations."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Expert System Recommendations")
    print("="*60)
    
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    expert_sys = GameExpertSystem(kb)
    
    # User preferences
    preferences = {
        "genres": ["RPG"],
        "difficulty": "Hard",
        "platforms": ["PC"]
    }
    
    print(f"\nGetting recommendations for:")
    for key, value in preferences.items():
        print(f"  {key}: {value}")
    
    recommendations = expert_sys.get_recommendations(preferences)
    
    print(f"\nTop recommendations:")
    for i, game in enumerate(recommendations, 1):
        print(f"\n{i}. {game['name']}")
        print(f"   Genres: {', '.join(game.get('genres', []))}")
        print(f"   Platforms: {', '.join(game.get('platforms', []))}")
        print(f"   Difficulty: {game.get('difficulty')}")


def example_multi_criteria_search():
    """Example: Complex multi-criteria search."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Multi-Criteria Search")
    print("="*60)
    
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    
    # Complex preferences
    criteria = {
        "genres": ["Action", "Adventure"],
        "multiplayer": "Single-player",
        "platforms": ["Nintendo Switch"],
        "game_length": "Long (30+ hours)"
    }
    
    print(f"\nSearching for games with criteria:")
    for key, value in criteria.items():
        print(f"  {key}: {value}")
    
    results = kb.search_games(criteria)
    
    print(f"\nFound {len(results)} matching games:")
    for game in results:
        print(f"  - {game['name']}")
        print(f"    Genres: {', '.join(game.get('genres', []))}")


def example_add_game():
    """Example: Add a new game to knowledge base."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Add New Game to Knowledge Base")
    print("="*60)
    
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    
    new_game = {
        "name": "The Witcher 3: Wild Hunt",
        "genres": ["RPG", "Action"],
        "multiplayer": "Single-player",
        "difficulty": "Hard",
        "platforms": ["PC", "PlayStation", "Xbox", "Nintendo Switch"],
        "graphics_style": "Realistic",
        "game_length": "Long (30+ hours)",
        "year": 2015,
        "description": "Open-world action RPG with monster hunting"
    }
    
    print(f"\nAdding game: {new_game['name']}")
    
    success = kb.add_game(new_game)
    
    if success:
        print(f"✓ Successfully added '{new_game['name']}' to knowledge base")
        print(f"Total games now: {len(kb.get_all_games())}")
    else:
        print(f"✗ Failed to add game (may already exist)")


def example_llm_integration():
    """Example: LLM integration for unknown games."""
    print("\n" + "="*60)
    print("EXAMPLE 5: LLM Integration (OpenRouter - Free Tier)")
    print("="*60)
    
    llm = LLMIntegration()
    
    if not llm.is_available():
        print("\n⚠️  LLM not available. Set OPENROUTER_API_KEY environment variable.")
        print("    Get a FREE key at: https://openrouter.ai/keys")
        print("    See SETUP_GUIDE.py for instructions.")
        return
    
    print("\n✓ LLM is available (OpenRouter Free Tier!)")
    
    # Try to get a recommendation
    preferences = {
        "genres": "RPG",
        "difficulty": "Medium",
        "platforms": "PC"
    }
    
    print(f"\nGetting LLM recommendation for:")
    for key, value in preferences.items():
        print(f"  {key}: {value}")
    
    recommendation = llm.recommend_game(preferences)
    
    if recommendation:
        print(f"\nLLM Recommendation:")
        print(recommendation)
    else:
        print("No recommendation from LLM")


def example_full_workflow():
    """Example: Full workflow with expert system and LLM fallback."""
    print("\n" + "="*60)
    print("EXAMPLE 6: Full Workflow (Expert System + LLM)")
    print("="*60)
    
    # Initialize components
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    expert_sys = GameExpertSystem(kb)
    llm = LLMIntegration()
    
    # User preferences
    preferences = {
        "genres": ["Puzzle"],
        "difficulty": "Easy",
        "game_length": "Short (< 10 hours)"
    }
    
    print(f"\nUser Preferences:")
    for key, value in preferences.items():
        print(f"  {key}: {value}")
    
    # Get expert system recommendations
    print(f"\nQuerying Expert System...")
    recommendations = expert_sys.get_recommendations(preferences)
    
    if recommendations:
        print(f"✓ Found {len(recommendations)} expert system recommendations:")
        for i, game in enumerate(recommendations, 1):
            print(f"  {i}. {game['name']}")
    else:
        print("✗ No expert system recommendations found")
        
        # Try LLM fallback
        if llm.is_available():
            print(f"\nQuerying LLM for fallback...")
            game_names = [g["name"] for g in kb.get_all_games()]
            fallback = llm.recommend_game(preferences, exclude_games=game_names)
            
            if fallback:
                print(f"✓ LLM Fallback Recommendation:")
                print(fallback)
        else:
            print("⚠️  LLM not available for fallback")


def example_display_all_games():
    """Example: Display all games in knowledge base."""
    print("\n" + "="*60)
    print("EXAMPLE 7: Display All Games in Knowledge Base")
    print("="*60)
    
    kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
    games = kb.get_all_games()
    
    print(f"\nTotal games in database: {len(games)}\n")
    
    for i, game in enumerate(games, 1):
        print(f"{i}. {game['name']} ({game['year']})")
        print(f"   Genres: {', '.join(game.get('genres', []))}")
        print(f"   Multiplayer: {game.get('multiplayer')}")
        print(f"   Platforms: {', '.join(game.get('platforms', []))}")
        print(f"   Length: {game.get('game_length')}")
        print()


def main():
    """Run all examples."""
    print("\n" + "🎮 EXPERT SYSTEM EXAMPLE USAGE 🎮".center(60))
    print("="*60)
    
    # Run examples
    example_basic_search()
    example_multi_criteria_search()
    example_expert_system()
    example_display_all_games()
    example_add_game()
    example_full_workflow()
    example_llm_integration()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)


if __name__ == "__main__":
    main()
