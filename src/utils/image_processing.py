# src/utils/gem_detector.py

import numpy as np
from config import Config

class GemDetector:
    def __init__(self):
        self.gem_colors = Config.GEMS_HSV
        self.tolerance = Config.COLOR_TOLERANCE

    def process_grid(self, hsv_grid):
        processed_grid = []
        for row in hsv_grid:
            processed_row = []
            for hsv_color in row:
                gem = self.detect_gem(hsv_color)
                processed_row.append(gem)
            processed_grid.append(processed_row)
        return processed_grid

    def detect_gem(self, hsv_color):
        h, s, v = hsv_color
        best_gem = None
        min_distance = float('inf')
        
        for gem, color in self.gem_colors.items():
            distance = self.color_distance(hsv_color, color)
            if distance < min_distance:
                min_distance = distance
                best_gem = gem

        if min_distance <= self.tolerance:
            return best_gem
        return None

    @staticmethod
    def color_distance(hsv1, hsv2):
        h1, s1, v1 = hsv1
        h2, s2, v2 = hsv2
        dh = min(abs(h1 - h2), 360 - abs(h1 - h2)) / 180.0
        ds = abs(s1 - s2) / 100.0
        dv = abs(v1 - v2) / 100.0
        return (dh**2 + ds**2 + dv**2)**0.5 * 100