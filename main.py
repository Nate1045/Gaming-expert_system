"""
Main entry point for the Game Recommendation Expert System.

A hybrid expert system that combines:
- EXPERTA: Rule-based reasoning engine
- LLM Integration: OpenRouter remote inference (free tier)
- PyQt6: Desktop GUI
- Knowledge Base: Game database with multiple criteria

Usage:
    python main.py
"""

from game_recommender.gui import main

if __name__ == "__main__":
    main()
