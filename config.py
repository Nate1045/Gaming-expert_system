"""
Configuration and constants for the expert system.
"""

# Game criteria options
GENRES = ["Action", "RPG", "Strategy", "Puzzle", "Adventure", "Sports", "Simulation", "Horror"]
MULTIPLAYER_TYPES = ["Single-player", "Local Co-op", "Online Multiplayer", "Competitive"]
DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
PLATFORMS = ["PC", "PlayStation", "Xbox", "Nintendo Switch", "Mobile"]
GRAPHICS_STYLES = ["Realistic", "Cartoon", "Pixel Art", "Anime"]
GAME_LENGTHS = ["Short (< 10 hours)", "Medium (10-30 hours)", "Long (30+ hours)"]

# LLM Configuration (OpenRouter free tier)
# Using llama-3.2-3b-instruct:free: fast, reliable, generous free tier
LLM_MODEL = "meta-llama/llama-3.2-3b-instruct:free"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 150

# Database settings
KNOWLEDGE_BASE_FILE = "data/games.json"

# GUI settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
