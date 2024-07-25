# src/gui/overlay.py

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRect
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

        # Draw grid
        pen = QPen(QColor(255, 255, 255, 50))  # White color with 50% opacity
        pen.setWidth(1)
        painter.setPen(pen)

        for i in range(1, Config.GRID_SIZE):
            # Vertical lines
            painter.drawLine(i * Config.BOX_SIZE, 0, i * Config.BOX_SIZE, self.height())
            # Horizontal lines
            painter.drawLine(0, i * Config.BOX_SIZE, self.width(), i * Config.BOX_SIZE)

        # Draw moves
        pen = QPen(QColor(255, 0, 0))  # Red color
        pen.setWidth(3)
        painter.setPen(pen)

        for move in self.moves:
            (r1, c1), (r2, c2) = move
            x1, y1 = c1 * Config.BOX_SIZE, r1 * Config.BOX_SIZE
            x2, y2 = c2 * Config.BOX_SIZE, r2 * Config.BOX_SIZE
            painter.drawLine(x1 + Config.BOX_SIZE // 2, y1 + Config.BOX_SIZE // 2, 
                             x2 + Config.BOX_SIZE // 2, y2 + Config.BOX_SIZE // 2)

    def update_moves(self, moves):
        self.moves = moves
        self.update()