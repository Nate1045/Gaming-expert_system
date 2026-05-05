"""
PyQt6 GUI for the expert system game recommendation application.
"""

import sys
from typing import List, Dict, Optional
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QTextEdit, QScrollArea,
    QCheckBox, QGroupBox, QGridLayout, QMessageBox, QDialog,
    QSpinBox, QDialogButtonBox, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QColor
from knowledge_base import GameKnowledgeBase
from expert_system import GameExpertSystem
from llm_integration import LLMIntegration
import config


class RecommendationDialog(QDialog):
    """Dialog for displaying game recommendations."""
    
    def __init__(self, parent, recommendations: List[Dict], llm_fallback: Optional[str] = None):
        super().__init__(parent)
        self.setWindowTitle("Game Recommendations")
        self.setGeometry(100, 100, 600, 500)
        self.recommendations = recommendations
        self.llm_fallback = llm_fallback
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("🎮 Recommended Games")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Results
        if self.recommendations:
            for i, game in enumerate(self.recommendations, 1):
                game_text = f"""
{i}. {game['name']}
   Genre: {', '.join(game.get('genres', []))}
   Platform: {', '.join(game.get('platforms', []))}
   Multiplayer: {game.get('multiplayer', 'N/A')}
   Length: {game.get('game_length', 'N/A')}
   Year: {game.get('year', 'N/A')}
   Description: {game.get('description', 'N/A')}
"""
                label = QLabel(game_text)
                label.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 5px;")
                layout.addWidget(label)
        else:
            no_results = QLabel("❌ No games found in knowledge base matching your criteria.")
            layout.addWidget(no_results)
        
        # LLM Fallback
        if self.llm_fallback:
            fallback_label = QLabel("\n🤖 LLM Recommendation (Not in Database):")
            fallback_font = QFont()
            fallback_font.setBold(True)
            fallback_label.setFont(fallback_font)
            layout.addWidget(fallback_label)
            
            llm_text = QTextEdit()
            llm_text.setText(self.llm_fallback)
            llm_text.setReadOnly(True)
            llm_text.setMaximumHeight(150)
            layout.addWidget(llm_text)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)


class GameExpertSystemGUI(QMainWindow):
    """Main GUI application for game recommendation expert system."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎮 Game Recommendation Expert System")
        self.setGeometry(100, 100, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        
        # Initialize backend
        self.kb = GameKnowledgeBase(config.KNOWLEDGE_BASE_FILE)
        self.expert_system = GameExpertSystem(self.kb)
        self.llm = LLMIntegration()
        
        # Initialize UI
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        
        # Left panel - Preferences
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.create_preferences_panel())
        
        # Right panel - Info and Results
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.create_info_panel())
        
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)
        
        central_widget.setLayout(main_layout)
    
    def create_preferences_panel(self) -> QGroupBox:
        """Create the preferences selection panel."""
        group = QGroupBox("Your Preferences")
        layout = QGridLayout()
        
        row = 0
        
        # Genres
        layout.addWidget(QLabel("📀 Genres (select multiple):"), row, 0, 1, 2)
        row += 1
        self.genre_checkboxes = {}
        for i, genre in enumerate(config.GENRES):
            checkbox = QCheckBox(genre)
            self.genre_checkboxes[genre] = checkbox
            layout.addWidget(checkbox, row + i // 2, i % 2)
        row += (len(config.GENRES) + 1) // 2 + 1
        
        # Multiplayer
        layout.addWidget(QLabel("👥 Multiplayer:"), row, 0)
        self.multiplayer_combo = QComboBox()
        self.multiplayer_combo.addItem("Any")
        for mp_type in config.MULTIPLAYER_TYPES:
            self.multiplayer_combo.addItem(mp_type)
        layout.addWidget(self.multiplayer_combo, row, 1)
        row += 1
        
        # Difficulty
        layout.addWidget(QLabel("⚔️ Difficulty:"), row, 0)
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItem("Any")
        for difficulty in config.DIFFICULTY_LEVELS:
            self.difficulty_combo.addItem(difficulty)
        layout.addWidget(self.difficulty_combo, row, 1)
        row += 1
        
        # Platforms
        layout.addWidget(QLabel("🖥️ Platforms (select multiple):"), row, 0, 1, 2)
        row += 1
        self.platform_checkboxes = {}
        for i, platform in enumerate(config.PLATFORMS):
            checkbox = QCheckBox(platform)
            self.platform_checkboxes[platform] = checkbox
            layout.addWidget(checkbox, row + i // 2, i % 2)
        row += (len(config.PLATFORMS) + 1) // 2 + 1
        
        # Graphics Style
        layout.addWidget(QLabel("🎨 Graphics Style:"), row, 0)
        self.graphics_combo = QComboBox()
        self.graphics_combo.addItem("Any")
        for style in config.GRAPHICS_STYLES:
            self.graphics_combo.addItem(style)
        layout.addWidget(self.graphics_combo, row, 1)
        row += 1
        
        # Game Length
        layout.addWidget(QLabel("⏱️ Game Length:"), row, 0)
        self.length_combo = QComboBox()
        self.length_combo.addItem("Any")
        for length in config.GAME_LENGTHS:
            self.length_combo.addItem(length)
        layout.addWidget(self.length_combo, row, 1)
        row += 1
        
        # Buttons
        layout.setSpacing(20)
        recommend_btn = QPushButton("🔍 Get Recommendations")
        recommend_btn.clicked.connect(self.get_recommendations)
        recommend_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px;")
        layout.addWidget(recommend_btn, row, 0, 1, 2)
        row += 1
        
        reset_btn = QPushButton("🔄 Reset")
        reset_btn.clicked.connect(self.reset_preferences)
        layout.addWidget(reset_btn, row, 0, 1, 2)
        
        group.setLayout(layout)
        return group
    
    def create_info_panel(self) -> QGroupBox:
        """Create the information display panel."""
        group = QGroupBox("Information & Results")
        layout = QVBoxLayout()
        
        # Title
        info_title = QLabel("Game Recommendation Expert System")
        info_title_font = QFont()
        info_title_font.setPointSize(12)
        info_title_font.setBold(True)
        info_title.setFont(info_title_font)
        layout.addWidget(info_title)
        
        # Description
        description = QLabel(
            "This hybrid system combines:\n\n"
            "✓ Expert System (EXPERTA) - Rule-based reasoning\n"
            "✓ LLM Integration (OpenRouter) - remote free-tier fallback\n"
            "✓ Knowledge Base - 10+ games initially\n\n"
            "Select your preferences and click 'Get Recommendations' to find the perfect game!"
        )
        layout.addWidget(description)
        
        # Knowledge base info
        kb_info = QLabel(f"\n📊 Knowledge Base Status:\n"
                        f"Total Games: {len(self.kb.get_all_games())}\n"
                        f"Hugging Face LLM: {'✓ Yes (Free Tier)' if self.llm.is_available() else '✗ No (Set HUGGINGFACE_API_KEY)'}")
        kb_info.setStyleSheet("background-color: #e3f2fd; padding: 10px; border-radius: 5px;")
        layout.addWidget(kb_info)
        
        # Manage Database button
        manage_btn = QPushButton("📚 Manage Database")
        manage_btn.clicked.connect(self.manage_database)
        layout.addWidget(manage_btn)
        
        # Results area
        results_label = QLabel("\n📋 Recommendation Results:")
        results_label_font = QFont()
        results_label_font.setBold(True)
        results_label.setFont(results_label_font)
        layout.addWidget(results_label)
        
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setText("Results will appear here...")
        layout.addWidget(self.results_text)
        
        group.setLayout(layout)
        return group
    
    def get_recommendations(self):
        """Get game recommendations based on selected preferences."""
        # Gather preferences
        preferences = {}
        
        # Get selected genres
        selected_genres = [genre for genre, checkbox in self.genre_checkboxes.items() 
                          if checkbox.isChecked()]
        if selected_genres:
            preferences["genres"] = selected_genres
        
        # Get multiplayer preference
        if self.multiplayer_combo.currentText() != "Any":
            preferences["multiplayer"] = self.multiplayer_combo.currentText()
        
        # Get difficulty preference
        if self.difficulty_combo.currentText() != "Any":
            preferences["difficulty"] = self.difficulty_combo.currentText()
        
        # Get selected platforms
        selected_platforms = [platform for platform, checkbox in self.platform_checkboxes.items() 
                             if checkbox.isChecked()]
        if selected_platforms:
            preferences["platforms"] = selected_platforms
        
        # Get graphics style preference
        if self.graphics_combo.currentText() != "Any":
            preferences["graphics_style"] = self.graphics_combo.currentText()
        
        # Get game length preference
        if self.length_combo.currentText() != "Any":
            preferences["game_length"] = self.length_combo.currentText()
        
        if not preferences:
            QMessageBox.warning(self, "No Preferences", "Please select at least one preference!")
            return
        
        # Get expert system recommendations
        recommendations = self.expert_system.get_recommendations(preferences)
        
        # If no recommendations, try LLM fallback
        llm_fallback = None
        if not recommendations and self.llm.is_available():
            game_names = [g["name"] for g in self.kb.get_all_games()]
            llm_fallback = self.llm.recommend_game(preferences, exclude_games=game_names)
        
        # Display results
        if recommendations:
            dialog = RecommendationDialog(self, recommendations, llm_fallback)
            dialog.exec()
        elif llm_fallback:
            dialog = RecommendationDialog(self, [], llm_fallback)
            dialog.exec()
        else:
            QMessageBox.information(self, "No Recommendations", 
                                   "No games found matching your preferences.\n"
                                   "Please adjust your criteria or configure LLM integration.")
    
    def reset_preferences(self):
        """Reset all preference selections."""
        for checkbox in self.genre_checkboxes.values():
            checkbox.setChecked(False)
        for checkbox in self.platform_checkboxes.values():
            checkbox.setChecked(False)
        self.multiplayer_combo.setCurrentIndex(0)
        self.difficulty_combo.setCurrentIndex(0)
        self.graphics_combo.setCurrentIndex(0)
        self.length_combo.setCurrentIndex(0)
        self.results_text.setText("Results will appear here...")
    
    def manage_database(self):
        """Open database management dialog."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Manage Game Database")
        dialog.setGeometry(200, 200, 500, 400)
        
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Current Games in Database:"))
        
        games_list = QListWidget()
        for game in self.kb.get_all_games():
            item_text = f"{game['name']} ({game['year']})"
            games_list.addItem(item_text)
        
        layout.addWidget(games_list)
        
        buttons_layout = QHBoxLayout()
        
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(lambda: self.update_games_list(games_list))
        buttons_layout.addWidget(refresh_btn)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        buttons_layout.addWidget(close_btn)
        
        layout.addLayout(buttons_layout)
        dialog.setLayout(layout)
        dialog.exec()
    
    def update_games_list(self, games_list):
        """Update the games list."""
        games_list.clear()
        for game in self.kb.get_all_games():
            item_text = f"{game['name']} ({game['year']})"
            games_list.addItem(item_text)


def main():
    """Run the application."""
    app = QApplication(sys.argv)
    window = GameExpertSystemGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
