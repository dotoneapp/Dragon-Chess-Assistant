# src/utils/image_processing.py
import numpy as np
from config import Config

class GemDetector:
    def __init__(self):
        self.gem_colors = Config.GEMS_HSV

    def hue_distance(self, h1, h2):
        diff = abs(h1 - h2)
        return min(diff, 360 - diff)

    def hsv_distance(self, hsv1, hsv2):
        h1, s1, v1 = hsv1
        h2, s2, v2 = hsv2
        dh = self.hue_distance(h1, h2) / 180.0  # Normalize to [0, 1]
        ds = abs(s1 - s2) / 100.0
        dv = abs(v1 - v2) / 100.0
        return np.sqrt(dh*dh + ds*ds + dv*dv)

    def detect_gem(self, color):
        distances = {gem: self.hsv_distance(color, hsv) for gem, hsv in self.gem_colors.items()}
        closest_gem = min(distances, key=distances.get)
        # The print statement has been removed from here
        return closest_gem

    def process_grid(self, grid):
        processed_grid = []
        for row in grid:
            processed_row = []
            for color in row:
                gem = self.detect_gem(color)
                processed_row.append(gem)
            processed_grid.append(processed_row)
        return processed_grid