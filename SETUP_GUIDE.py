"""
SETUP GUIDE - Getting Started with the Expert System

This file provides step-by-step instructions to get the application running.
"""

# ============================================================================
# INSTALLATION & SETUP GUIDE
# ============================================================================

"""
STEP 1: Install Dependencies
================================

1. Open PowerShell/Command Prompt in the project directory

2. Create a Python virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

4. Install required packages:
   pip install -r requirements.txt

   This will install:
   - experta (1.9.2) - Expert system framework
   - requests (2.31.0+) - OpenRouter inference client (free remote LLM)
   - PyQt6 (6.11.0) - GUI framework


STEP 2: Configure OpenRouter API (Optional, FREE TIER)
=======================================================

For LLM fallback features, you need a free OpenRouter API key:

1. Get a free API key from: https://openrouter.ai/keys
   - No credit card required for the free tier
   - Instant account creation
   - Generous free inference quota for personal use

2. Set the environment variable:

   Windows (PowerShell):
   $env:OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"

   Windows (Command Prompt):
   set OPENROUTER_API_KEY=sk-or-v1-your-api-key-here

   Mac/Linux:
   export OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"

   Mac/Linux:
   export HUGGINGFACE_API_KEY="hf_your-api-token-here"

3. Note: The system works without LLM, but recommendations are limited to
   the knowledge base only. With LLM, unknown games can be recommended.


STEP 3: Run the Application
=============================

From the project directory with venv activated:
python main.py

This will launch the PyQt6 desktop application.


STEP 4: Using the Application
===============================

1. Select your gaming preferences:
   - Check genres you enjoy (Action, RPG, Puzzle, etc.)
   - Choose multiplayer type (Single-player, Local Co-op, etc.)
   - Select difficulty level
   - Pick your platforms (PC, PlayStation, Nintendo, etc.)
   - Choose graphics style preference
   - Select how long you want to play

2. Click "Get Recommendations"

3. View results:
   - Expert system recommendations from knowledge base
   - LLM fallback recommendations (if available)
   - Detailed game information

4. Manage Database:
   - Click "Manage Database" to view all games
   - See what's in the knowledge base


PROJECT STRUCTURE
=================

main.py                  - Entry point for the application
                         - Imports and runs the GUI

config.py              - All configuration & constants
                       - Criteria options, LLM settings, GUI dimensions

knowledge_base.py      - Game database management
                       - Load/save games, search, add/update/delete

expert_system.py       - EXPERTA rule-based engine
                       - 6+ rules for different gaming preferences

llm_integration.py     - Hugging Face inference integration
                       - LLM recommendations & game information extraction

gui.py                 - PyQt6 desktop interface
                       - Preference selection, results display

requirements.txt       - Python package dependencies

README.md              - Comprehensive documentation

data/
  └── games.json       - Game knowledge base (auto-created)


INITIAL KNOWLEDGE BASE (10 GAMES)
=================================

1. The Legend of Zelda: Breath of the Wild (Adventure/Action)
2. Elden Ring (RPG/Action)
3. Portal 2 (Puzzle)
4. Super Smash Bros. Ultimate (Fighting/Sports)
5. Civilization VI (Strategy)
6. Hades (Action/RPG)
7. Stardew Valley (Simulation)
8. Among Us (Strategy/Social)
9. Resident Evil Village (Horror/Action)
10. Hollow Knight (Action/Adventure)


CUSTOMIZATION
==============

To add/modify criteria:
1. Edit config.py - Add new criteria to lists
2. Update knowledge_base.py - Add new search filters
3. Update expert_system.py - Add new rules
4. Update gui.py - Add new UI elements

To add new games:
1. Edit data/games.json manually, OR
2. Use the database manager in the GUI, OR
3. Let LLM extract game info and add it


SYSTEM REQUIREMENTS
===================

- Python 3.8 or higher
- ~100MB disk space
- Internet connection (for LLM features)
- Display capable of PyQt6 rendering


TROUBLESHOOTING
===============

Issue: "ModuleNotFoundError: No module named 'experta'"
Solution: Ensure virtual environment is activated and requirements installed
         pip install -r requirements.txt

Issue: GUI doesn't appear or crashes
Solution: Update PyQt6
         pip install --upgrade PyQt6

Issue: LLM features not working
Solution: Check OpenAI API key is set and valid
         $env:OPENAI_API_KEY (to verify on Windows PowerShell)

Issue: Knowledge base not saving
Solution: Ensure data/ directory exists and has write permissions
         Check disk space available


FEATURES OVERVIEW
==================

Expert System Features:
✓ Rule-based reasoning (EXPERTA)
✓ 6+ specialized recommendation rules
✓ Fact-based game matching
✓ Conflict resolution

LLM Integration:
✓ Fallback for unknown games
✓ Game information extraction
✓ Natural language recommendations
✓ Optional game database updates

Knowledge Base:
✓ 10+ initial games
✓ Multi-criteria search
✓ Add/update/delete operations
✓ JSON persistence

GUI Features:
✓ Multiple preference options
✓ Real-time filtering
✓ Results display
✓ Database management


ARCHITECTURE HIGHLIGHTS
=======================

Modular Design:
- Each component is independent
- Easy to test and extend
- Clear separation of concerns

Hybrid Approach:
- Expert system handles known games
- LLM provides flexible recommendations
- Best of both symbolic and neural AI

Extensible:
- Add new criteria easily
- Integrate different LLM providers
- Modify rules without code changes


NEXT STEPS
==========

1. Run: python main.py
2. Try different preference combinations
3. Review game details
4. Explore LLM recommendations (if API key set)
5. Check README.md for detailed documentation


SUPPORT & DOCUMENTATION
=======================

See README.md for:
- Complete architecture overview
- Detailed feature descriptions
- Expert system rules explanation
- LLM integration details
- Future enhancement ideas

---
Ready to explore! 🎮
"""

if __name__ == "__main__":
    print(__doc__)
