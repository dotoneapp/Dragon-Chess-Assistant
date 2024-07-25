# tests/test_game_logic.py

import unittest
from src.utils.image_processing import GemDetector
import numpy as np

class TestGemDetector(unittest.TestCase):
    def setUp(self):
        self.detector = GemDetector()

    def test_detect_gem(self):
        self.assertEqual(self.detector.detect_gem([255, 0, 0]), 'red')
        self.assertEqual(self.detector.detect_gem([0, 0, 255]), 'blue')
        self.assertEqual(self.detector.detect_gem([0, 255, 0]), 'green')
        self.assertEqual(self.detector.detect_gem([255, 255, 0]), 'yellow')
        self.assertEqual(self.detector.detect_gem([255, 0, 255]), 'purple')
        self.assertIsNone(self.detector.detect_gem([100, 100, 100]))

    def test_process_grid(self):
        mock_grid = [
            [[255, 0, 0], [0, 255, 0]],
            [[0, 0, 255], [255, 255, 0]]
        ]
        expected_output = [
            ['red', 'green'],
            ['blue', 'yellow']
        ]
        self.assertEqual(self.detector.process_grid(mock_grid), expected_output)

if __name__ == '__main__':
    unittest.main()