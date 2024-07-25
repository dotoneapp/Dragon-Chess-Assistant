# src/gui/main_window.py

from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt, QPoint
from gui.overlay import Overlay
from gui.debug_window import DebugWindow
from config import Config, base64_string
import base64

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(769, 257)
        self.dragging = False
        self.init_ui()

    def init_ui(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(769, 257)
        self.dragging = False
        self.init_ui()

    def init_ui(self):
        # Decode the base64 image
        image_data = base64.b64decode(base64_string)
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        # Set the background image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 769, 257)
        
        # Create and style the toggle button
        self.toggle_button = QPushButton('START', self)
        self.toggle_button.setGeometry(224, 131, 320, 66)
        self.toggle_button.setCheckable(True)
        self.set_button_style('green')
        self.toggle_button.clicked.connect(self.toggle_assistant)

        # Create and style the labels
        self.dragon_chess_label = QLabel('DRAGON CHESS IS READY', self)
        self.dragon_chess_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dragon_chess_label.setGeometry(274, 22, 221, 18)
        self.dragon_chess_label.setStyleSheet("""
            color: #ABABAB;
            font-size: 16px;
            font-family: Arial;
            font-weight: semibold;
        """)

        self.all_moves_label = QLabel('ALL MOVES', self)
        self.all_moves_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.all_moves_label.setGeometry(310, 48, 148, 22)
        self.all_moves_label.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-family: Arial;
            font-weight: bold;
        """)

        self.close_label = QLabel('⛒︎ Close', self)
        self.close_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.close_label.setGeometry(769 - 22 - 70, 257 - 24 - 22, 70, 22)
        self.close_label.setStyleSheet("""
            color: #ABABAB;
            font-size: 14px;
            font-family: Arial;
        """)
        self.close_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_label.mousePressEvent = self.close_window
        
        self.overlay = Overlay()
        self.assistant_active = False

        # Add debug button
        self.debug_button = QPushButton('Debug', self)
        self.debug_button.setGeometry(669, 22, 80, 30)
        self.debug_button.clicked.connect(self.toggle_debug_window)

        self.overlay = Overlay()
        self.debug_window = DebugWindow()
        self.assistant_active = False
        self.debug_active = False

    def toggle_debug_window(self):
        if not self.debug_active:
            self.debug_window.show()
            self.debug_active = True
        else:
            self.debug_window.hide()
            self.debug_active = False

    def set_button_style(self, color):
        styles = {
            'green': """
                QPushButton {
                    font-size: 24px;
                    font-family: Arial;
                    font-weight: bold;
                    color: white;
                    border-radius: 3px;
                    border: 2px solid #435f4f;
                    background: qradialgradient(cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0 #435f4f, stop:1 #2d3e36);
                }
                QPushButton:hover {
                    background: qradialgradient(cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0 #4f6d5e, stop:1 #3a4c40);
                }
            """,
            'red': """
                QPushButton {
                    font-size: 24px;
                    font-family: Arial;
                    font-weight: bold;
                    color: white;
                    border-radius: 3px;
                    border: 2px solid #8e2b19;
                    background: qradialgradient(cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0 #6b211c, stop:1 #550003);
                }
                QPushButton:hover {
                    background: qradialgradient(cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.5, stop:0 #772f2b, stop:1 #620e0d);
                }
            """
        }
        self.toggle_button.setStyleSheet(styles[color])

    def toggle_assistant(self):
        if not self.assistant_active:
            self.start_assistant()
        else:
            self.stop_assistant()

    def start_assistant(self):
        self.assistant_active = True
        self.toggle_button.setText('STOP')
        self.set_button_style('red')
        self.overlay.show()

    def stop_assistant(self):
        self.assistant_active = False
        self.toggle_button.setText('START')
        self.set_button_style('green')
        self.overlay.hide()

    def close_window(self, event):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToGlobal(event.position().toPoint() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
    
    