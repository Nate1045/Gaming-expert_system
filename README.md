# 🎮 Game Recommendation Expert System

A hybrid game recommendation system that combines a rules-driven expert system with optional OpenRouter LLM fallback.

## Overview

This project includes:
- `PyQt6` desktop GUI
- `experta` expert system reasoning
- `requests` for OpenRouter LLM integration
- A JSON game knowledge base for deterministic recommendations

## Features

- Rule-based recommendations using `experta`
- Package-centric architecture under `game_recommender/`
- Optional OpenRouter fallback for new or unmatched game suggestions
- JSON-backed knowledge base with persistence
- Desktop UI for preferences and results

## Requirements

- Python 3.8 or higher
- `experta==1.9.2`
- `frozendict==1.2`
- `requests>=2.31.0`
- `PyQt6==6.11.0`

## Project Structure

```
expert-system/
├── main.py
├── examples.py
├── README.md
├── data/
│   └── games.json
└── game_recommender/
    ├── __init__.py
    ├── config.py
    ├── expert_system.py
    ├── gui.py
    ├── knowledge_base.py
    └── llm_integration.py
```

## Installation

### 1. Open the project directory

```bash
cd expert-system
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Configure OpenRouter (optional)

OpenRouter is optional but recommended for fallback LLM recommendations.

```bash
# Get a free API key at: https://openrouter.ai/keys
```

Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"
```

Windows CMD:

```cmd
set OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
```

Mac/Linux:

```bash
export OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"
```

### 4. Run the application

```bash
python main.py
```

## Usage

1. Select genres, multiplayer, difficulty, platforms, graphics style, and game length.
2. Click **Get Recommendations**.
3. Review the recommended games in the dialog.
4. If no database match exists, OpenRouter can provide fallback suggestions.
5. Use **Manage Database** to inspect stored games.

## Configuration

Customize recommendation criteria and GUI settings in `game_recommender/config.py`.

## Knowledge Base

The app uses `data/games.json` to store games. The knowledge base is auto-created if missing.

### Initial Games
- The Legend of Zelda: Breath of the Wild
- Elden Ring
- Portal 2
- Super Smash Bros. Ultimate
- Civilization VI
- Hades
- Stardew Valley
- Among Us
- Resident Evil Village
- Hollow Knight
- The Witcher 3: Wild Hunt

## LLM Integration

This project currently uses OpenRouter for optional fallback recommendations.

- No database match found
- LLM fallback enabled via `OPENROUTER_API_KEY`
- Returns natural language game suggestions

---
## Troubleshooting

### LLM Features Not Working
- Verify OPENROUTER_API_KEY environment variable is set
- Get free API key from: https://openrouter.ai/keys
- Check internet connection
- Verify API key validity (starts with `sk-or-v1-`)
- Check OpenRouter API rate limits

### GUI Not Appearing
- Verify PyQt6 installation: `pip install --upgrade PyQt6`
- Check display/X11 forwarding if on remote system

### Knowledge Base Not Persisting
- Verify `data/` directory has write permissions
- Check disk space
- Ensure games.json is not corrupted

## Future Enhancements

1. **Database Enhancements**
   - User ratings/reviews
   - Play history tracking
   - Wishlist functionality

2. **Expert System Improvements**
   - Machine learning integration
   - User behavior learning
   - Personalized recommendation scoring

3. **LLM Integration**
   - Support for Claude, Llama models
   - Fine-tuned models for gaming domain
   - Streaming recommendations

4. **GUI Enhancements**
   - Dark mode theme
   - Game images/thumbnails
   - Recommendation history
   - Favorites system

5. **Web Version**
   - Flask/FastAPI backend
   - React frontend
   - Cloud database

## Dependencies

- **experta** (1.9.2): Expert system framework
- **requests** (2.31.0+): OpenRouter inference client
- **PyQt6** (6.11.0): GUI framework

