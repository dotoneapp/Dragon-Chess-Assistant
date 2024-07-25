# tests/test_screen_reader.py

import unittest
from src.screen_reader.screen_capture import ScreenCapture
from PIL import Image
import numpy as np

class TestScreenCapture(unittest.TestCase):
    def setUp(self):
        self.capture = ScreenCapture(x=0, y=0, width=100, height=100)

    def test_capture(self):
        img = self.capture.capture()
        self.assertIsInstance(img, Image.Image)
        self.assertEqual(img.size, (100, 100))

    def test_get_grid(self):
        grid = self.capture.get_grid(rows=8, cols=8)
        self.assertEqual(len(grid), 8)
        self.assertEqual(len(grid[0]), 8)
        self.assertIsInstance(grid[0][0], np.ndarray)
        self.assertEqual(len(grid[0][0]), 3)  # RGB values

if __name__ == '__main__':
    unittest.main()