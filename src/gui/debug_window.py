# src/gui/debug_window.py

from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
from config import Config

class DebugWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gem Detection Debug")
        self.setGeometry(100, 100, 400, 400)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.gem_colors = {
            "R": QColor(255, 0, 0),    # Red
            "P": QColor(128, 0, 128),  # Purple
            "G": QColor(0, 255, 0),    # Green
            "Y": QColor(255, 255, 0),  # Yellow
            "B": QColor(0, 0, 255),    # Blue
            "O": QColor(255, 165, 0),  # Orange
            None: QColor(128, 128, 128)  # Gray for unknown
        }

        self.labels = [[QLabel() for _ in range(Config.GRID_SIZE)] for _ in range(Config.GRID_SIZE)]
        for i in range(Config.GRID_SIZE):
            for j in range(Config.GRID_SIZE):
                label = self.labels[i][j]
                label.setFixedSize(40, 40)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.grid_layout.addWidget(label, i, j)

    def update_grid(self, gem_grid):
        for i in range(Config.GRID_SIZE):
            for j in range(Config.GRID_SIZE):
                gem = gem_grid[i][j]
                label = self.labels[i][j]
                color = self.gem_colors.get(gem, self.gem_colors[None])
                palette = label.palette()
                palette.setColor(QPalette.ColorRole.Window, color)
                label.setAutoFillBackground(True)
                label.setPalette(palette)
                label.setText(str(gem) if gem else "")