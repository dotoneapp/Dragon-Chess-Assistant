# src/utils/image_processing.py

import numpy as np

class GemDetector:
    def __init__(self):
        # Define color ranges for each gem type
        # These values need to be adjusted based on the actual colors in your game
        self.gem_colors = {
            'red': ([150, 0, 0], [255, 100, 100]),
            'blue': ([0, 0, 150], [100, 100, 255]),
            'green': ([0, 150, 0], [100, 255, 100]),
            'yellow': ([150, 150, 0], [255, 255, 100]),
            'purple': ([150, 0, 150], [255, 100, 255]),
            # Add more colors as needed
        }

    def detect_gem(self, color):
        for gem_type, (lower, upper) in self.gem_colors.items():
            if np.all(color >= lower) and np.all(color <= upper):
                return gem_type
        return None

    def process_grid(self, grid):
        processed_grid = []
        for row in grid:
            processed_row = []
            for color in row:
                gem = self.detect_gem(color)
                processed_row.append(gem)
            processed_grid.append(processed_row)
        return processed_grid

# Example usage
if __name__ == "__main__":
    detector = GemDetector()
    # This is a mock grid, replace with actual data from ScreenCapture
    mock_grid = [
        [[255, 0, 0], [0, 255, 0]],
        [[0, 0, 255], [255, 255, 0]]
    ]
    processed_grid = detector.process_grid(mock_grid)
    print(processed_grid)