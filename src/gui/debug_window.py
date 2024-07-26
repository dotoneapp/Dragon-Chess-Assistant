# src/gui/debug_window.py

from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class DebugWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debug: Detected Grid")
        self.setGeometry(100, 100, 400, 400)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.cells = []
        self.init_grid()

    def init_grid(self):
        for i in range(8):
            row = []
            for j in range(8):
                label = QLabel()
                label.setFixedSize(50, 50)  # Increased size for more information
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("border: 1px solid black; font-size: 8px;")  # Smaller font for more info
                self.grid_layout.addWidget(label, i, j)
                row.append(label)
            self.cells.append(row)

    def update_grid(self, gem_grid, hsv_grid):
        for i in range(8):
            for j in range(8):
                gem = gem_grid[i][j]
                hsv = hsv_grid[i][j]
                label = self.cells[i][j]
                
                h, s, v = hsv
                
                label.setText(f"Gem: {gem}\nH:{h}\nS:{s}%\nV:{v}%")
                
                # Set background color based on HSV
                qcolor = QColor.fromHsv(h, int(s * 2.55), int(v * 2.55))  # QColor uses 0-255 for S and V
                label.setStyleSheet(f"background-color: {qcolor.name()}; border: 1px solid black; font-size: 8px; color: {'black' if v > 50 else 'white'};")

    def get_color(self, gem):
        color_map = {
            'R': '#FF0000',  # Red
            'P': '#800080',  # Purple
            'G': '#008000',  # Green
            'Y': '#FFFF00',  # Yellow
            'B': '#0000FF',  # Blue
            'O': '#FFA500',  # Orange
            None: '#FFFFFF'  # White for empty cells
        }
        return color_map.get(gem, '#FFFFFF')