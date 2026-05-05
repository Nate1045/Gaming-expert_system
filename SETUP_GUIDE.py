"""
SETUP GUIDE - Getting Started with the Expert System

This file provides step-by-step instructions to get the application running.
"""

# ============================================================================
# INSTALLATION & SETUP GUIDE
# ============================================================================

"""
STEP 1: Create & Activate a Virtual Environment
===============================================

1. Open PowerShell or Command Prompt in the project directory.

2. Create a Python virtual environment:
   python -m venv .venv

3. Activate the virtual environment:
   - Windows PowerShell: .venv\Scripts\Activate.ps1
   - Windows CMD: .venv\Scripts\activate.bat
   - Mac/Linux: source .venv/bin/activate

STEP 2: Install Dependencies
============================

4. Install required packages:
   pip install -r requirements.txt

   This will install:
   - experta==1.9.2          # Expert system framework
   - frozendict==1.2         # Compatibility fix for experta on newer Python
   - requests>=2.31.0        # OpenRouter remote LLM client
   - PyQt6==6.11.0           # Desktop GUI framework

STEP 3: Configure OpenRouter API (Optional)
===========================================

For LLM fallback features, set the OpenRouter API key. The app works without LLM, but OpenRouter enables richer recommendations.

1. Get a free API key from: https://openrouter.ai/keys

2. Set the environment variable:

   Windows PowerShell:
   $env:OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"

   Windows CMD:
   set OPENROUTER_API_KEY=sk-or-v1-your-api-key-here

   Mac/Linux:
   export OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"

STEP 4: Launch the Application
==============================

From the project directory with the virtual environment activated:
   python main.py

This launches the PyQt6 desktop application.

STEP 5: Using the Application
=============================

1. Choose your gaming preferences:
   - Genres
   - Multiplayer type
   - Difficulty
   - Platforms
   - Graphics style
   - Game length

2. Click "Get Recommendations"
3. View results in the recommendation dialog
4. If no match is found, OpenRouter may provide a fallback recommendation
5. Use "Manage Database" to view the stored games

PROJECT STRUCTURE
=================

main.py                    - Entry point for the application
examples.py                - Usage examples and programmatic usage
requirements.txt           - Python package dependencies
README.md                  - Project documentation
SETUP_GUIDE.py             - This setup guide

data/
  └── games.json           - Game knowledge base (auto-created)

game_recommender/
  ├── __init__.py
  ├── config.py            - Configuration constants and criteria
  ├── expert_system.py     - EXPERTA rule-based recommendation engine
  ├── gui.py               - PyQt6 interface and main application UI
  ├── knowledge_base.py    - JSON knowledge base management
  └── llm_integration.py   - OpenRouter LLM fallback integration

INITIAL KNOWLEDGE BASE (10 GAMES)
=================================

1. The Legend of Zelda: Breath of the Wild
2. Elden Ring
3. Portal 2
4. Super Smash Bros. Ultimate
5. Civilization VI
6. Hades
7. Stardew Valley
8. Among Us
9. Resident Evil Village
10. Hollow Knight

CUSTOMIZATION
==============

To update recommendation criteria:
1. Edit `game_recommender/config.py`
2. Update search logic in `game_recommender/knowledge_base.py`
3. Add or adjust rules in `game_recommender/expert_system.py`
4. Update UI inputs in `game_recommender/gui.py`

To add new games:
- Edit `data/games.json` manually
- Use the database manager in the GUI
- Extend the app to import new games programmatically

SYSTEM REQUIREMENTS
===================

- Python 3.8 or higher
- ~100MB disk space
- Internet connection for LLM features
- Display capable of PyQt6 rendering

TROUBLESHOOTING
===============

Issue: "ModuleNotFoundError: No module named 'experta'"
Solution: Activate the virtual environment and install dependencies:
   pip install -r requirements.txt

Issue: GUI does not start
Solution: Confirm PyQt6 is installed and compatible with your Python version.

Issue: LLM fallback is not working
Solution: Ensure `OPENROUTER_API_KEY` is set and valid.

Issue: Knowledge base not saving
Solution: Confirm the `data/` directory exists and is writable.

FEATURE HIGHLIGHTS
==================

- Hybrid rule-based + LLM recommendation architecture
- Package-based layout under `game_recommender/`
- JSON knowledge base with persistence
- Optional OpenRouter fallback for unknown games
- Desktop UI built with PyQt6

NEXT STEPS
==========

1. Run `python main.py`
2. Choose preferences
3. Review recommendations
4. Enable OpenRouter for fallback suggestions
5. Explore and extend the knowledge base

---
"""

if __name__ == "__main__":
    print(__doc__)
