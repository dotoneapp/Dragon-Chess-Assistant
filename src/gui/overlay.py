# src/gui/overlay.py

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt
from config import Config

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(Config.GRID_START_X, Config.GRID_START_Y, 
                         Config.GRID_SIZE * Config.BOX_SIZE, 
                         Config.GRID_SIZE * Config.BOX_SIZE)
        self.moves = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Set up the pen for drawing
        pen = QPen(QColor(255, 255, 255))  # White color
        pen.setWidth(2)  # Thin line
        painter.setPen(pen)

        # Draw rounded rectangles around valid moves
        for move in self.moves:
            (r1, c1), (r2, c2) = move
            x1, y1 = c1 * Config.BOX_SIZE, r1 * Config.BOX_SIZE
            x2, y2 = c2 * Config.BOX_SIZE, r2 * Config.BOX_SIZE
            
            # Calculate the bounding rectangle for both gems
            left = min(x1, x2)
            top = min(y1, y2)
            width = Config.BOX_SIZE * 2 if c1 != c2 else Config.BOX_SIZE
            height = Config.BOX_SIZE * 2 if r1 != r2 else Config.BOX_SIZE
            
            # Draw a rounded rectangle around both gems
            painter.drawRoundedRect(left, top, width, height, 10, 10)

    def update_moves(self, moves):
        self.moves = moves
        self.update()