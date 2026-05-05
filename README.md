# 🎮 Game Recommendation Expert System - Hybrid LLM Architecture

A sophisticated game recommendation system combining rule-based expert systems (EXPERTA) with LLM capabilities for intelligent game suggestions.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    PyQt6 Desktop GUI                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │ Preferences Panel    │  │ Results & Information Panel      │ │
│  │ - Genres             │  │ - Display Recommendations        │ │
│  │ - Multiplayer        │  │ - LLM Fallback Results           │ │
│  │ - Difficulty         │  │ - Database Management            │ │
│  │ - Platforms          │  │ - System Status                  │ │
│  │ - Graphics Style     │  │                                  │ │
│  │ - Game Length        │  │                                  │ │
│  └──────────────────────┘  └──────────────────────────────────┘ │
│           ↓                              ↑                       │
└─────────────────────────────────────────────────────────────────┘
                  ↓
      ┌───────────────────────┐
      │  Recommendation Engine│
      └─────────┬─────────────┘
                │
        ┌───────┴──────────┐
        ↓                  ↓
   ┌─────────────┐    ┌─────────────────┐
   │Expert System│    │LLM Integration  │
   │  (EXPERTA)  │    │(OpenAI GPT-3.5) │
   │  - Rules    │    │- Fallback       │
   │  - Facts    │    │- New Games      │
   └──────┬──────┘    └────────┬────────┘
          │                    │
          └────────┬───────────┘
                   ↓
          ┌──────────────────┐
          │ Knowledge Base   │
          │  (JSON Database) │
          │  - 10+ Games     │
          │  - Searchable    │
          │  - Updatable     │
          └──────────────────┘
```

## Features

### 1. **Expert System (EXPERTA)**
- Rule-based reasoning for game recommendations
- 6 primary rules covering different gaming preferences:
  - Action games for single-player fans
  - Challenging RPGs
  - Multiplayer experiences
  - Puzzle games
  - Short gaming sessions
  - Long-form gaming adventures
  - Mobile gaming recommendations

### 2. **Game Recommendation Criteria** (6+)
- **📀 Genres**: Action, RPG, Strategy, Puzzle, Adventure, Sports, Simulation, Horror
- **👥 Multiplayer**: Single-player, Local Co-op, Online Multiplayer, Competitive
- **⚔️ Difficulty**: Easy, Medium, Hard
- **🖥️ Platforms**: PC, PlayStation, Xbox, Nintendo Switch, Mobile
- **🎨 Graphics Style**: Realistic, Cartoon, Pixel Art, Anime
- **⏱️ Game Length**: Short (< 10 hours), Medium (10-30 hours), Long (30+ hours)

### 3. **LLM Integration (OpenRouter Free Tier)**
- Completely free with OpenRouter token
- Fallback recommendation when no games match in knowledge base
- Game information extraction for new entries
- Natural language recommendations with reasoning
- Optional: Add recommended games to knowledge base
- Uses llama-3.2-3b-instruct:free model via OpenRouter remote inference (fast & reliable)

### 4. **Knowledge Base**
- Initial 10 curated games
- JSON-based persistence
- Search functionality with multiple criteria
- Add/Update/Delete game operations
- Automatic ID management

### 5. **PyQt6 Desktop GUI**
- Intuitive preference selection
- Real-time filtering
- Results display with game details
- Database management interface
- System status monitoring

## Project Structure

```
expert-system/
├── main.py                 # Entry point
├── config.py              # Configuration & constants
├── knowledge_base.py      # Game database management
├── expert_system.py       # EXPERTA rules engine
├── llm_integration.py     # Hugging Face integration
├── gui.py                 # PyQt6 interface
├── requirements.txt       # Dependencies
├── README.md              # This file
└── data/
    └── games.json         # Game knowledge base
```

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (optional, for LLM features)

### Setup Steps

1. **Clone/Extract the project**
```bash
cd expert-system
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set OpenRouter API key (optional, for LLM features)**
```bash
# Get free API key at: https://openrouter.ai/keys

# Windows PowerShell
$env:OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"

# Windows CMD
set OPENROUTER_API_KEY=sk-or-v1-your-api-key-here

# Linux/Mac
export OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"
```

5. **Run the application**
```bash
python main.py
```

## Usage

1. **Select Preferences**: Choose one or more criteria from the left panel
2. **Get Recommendations**: Click "Get Recommendations"
3. **View Results**: Recommended games appear in a dialog with details
4. **LLM Fallback**: If no matches found, LLM provides recommendations
5. **Manage Database**: View and manage stored games

### Example Workflow

1. Check "Action" and "RPG" genres
2. Select "Hard" difficulty
3. Choose "PC" platform
4. Click "Get Recommendations"
5. View matching games or LLM suggestions

## Modular Architecture Benefits

### Separation of Concerns
- **config.py**: All constants in one place
- **knowledge_base.py**: Database operations isolated
- **expert_system.py**: Pure rule-based logic
- **llm_integration.py**: LLM communication
- **gui.py**: User interface
- **main.py**: Orchestration

### Extensibility
- Add new rules to expert system
- Add new games to knowledge base
- Integrate different LLM providers
- Extend GUI with new features
- Modify criteria/attributes easily

### Testability
- Each module can be tested independently
- Mock LLM for testing
- Create test knowledge bases
- Validate rules in isolation

## Configuration

Edit `config.py` to customize:

```python
# Game criteria options
GENRES = [...]
MULTIPLAYER_TYPES = [...]
DIFFICULTY_LEVELS = [...]
PLATFORMS = [...]
GRAPHICS_STYLES = [...]
GAME_LENGTHS = [...]

# LLM settings
LLM_MODEL = "gpt-3.5-turbo"
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 500

# GUI settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
```

## Game Knowledge Base

### Initial Games (10)
1. **The Legend of Zelda: Breath of the Wild** - Adventure
2. **Elden Ring** - RPG, Action
3. **Portal 2** - Puzzle
4. **Super Smash Bros. Ultimate** - Fighting
5. **Civilization VI** - Strategy
6. **Hades** - Action, RPG
7. **Stardew Valley** - Simulation
8. **Among Us** - Strategy, Social
9. **Resident Evil Village** - Horror, Action
10. **Hollow Knight** - Action, Adventure

### Adding Games

Games can be added through:
1. Direct database management (via GUI)
2. LLM extraction of new game information
3. JSON file editing

## LLM Integration Details

### Hugging Face API (Free Tier)
- **Provider**: Hugging Face Inference API
- **Cost**: Free tier available for personal use
- **Model**: google/flan-t5-large
- **Why Hugging Face**: Remote inference with a free API token
- **Get Started**: https://huggingface.co/settings/tokens

### When LLM is Used
- No expert system matches found
- User wants to explore beyond knowledge base
- Gathering information about new games

### LLM Capabilities
- Game recommendations with reasoning
- Game information extraction
- Validation of game attributes
- Natural language explanations

### Example LLM Response
```
"I'd recommend 'Baldur's Gate 3' for you!

Since you enjoy challenging RPGs and prefer PC gaming, 
Baldur's Gate 3 is perfect. It offers:
- Complex tactical combat (challenging gameplay)
- Deep story-driven RPG experience
- Mod support for PC players
- 100+ hours of content

This is not currently in our database. Would you like 
me to add it?"
```

## Expert System Rules

### Rule 1: Action Single-Player
- Triggers: Action genre + Single-player
- Effect: Filter for action single-player games

### Rule 2: Challenging RPG
- Triggers: RPG genre + Hard difficulty
- Effect: Filter for challenging RPGs

### Rule 3: Multiplayer Focus
- Triggers: Local Co-op OR Online Multiplayer
- Effect: Filter for multiplayer experiences

### Rule 4: Puzzle Games
- Triggers: Puzzle genre + (Easy OR Medium difficulty)
- Effect: Filter for accessible puzzles

### Rule 5: Short Sessions
- Triggers: Short game length < 10 hours
- Effect: Filter for quick-play games

### Rule 6: Long-Form Experience
- Triggers: Long game length 30+ hours
- Effect: Filter for extended gaming experiences

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

## License

This project is provided as-is for educational and personal use.

## Author

Created as a comprehensive example of hybrid AI system architecture combining symbolic reasoning and neural networks.

---

**Happy Gaming! 🎮**
