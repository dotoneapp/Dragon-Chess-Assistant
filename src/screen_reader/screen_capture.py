# src/screen_reader/screen_capture.py

import mss
import numpy as np
from PIL import Image
import colorsys

class ScreenCapture:
    def __init__(self, x, y, width, height):
        self.bbox = {'top': y, 'left': x, 'width': width, 'height': height}
        self.sct = mss.mss()

    def capture(self):
        # Capture the specified area of the screen
        sct_img = self.sct.grab(self.bbox)
        # Convert to PIL Image
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        return img

    def get_grid(self, rows=8, cols=8):
        # Capture the screen
        original_img = self.capture()
        
        # Resize the image to 8x8 pixels without any processing
        resized_img = original_img.resize((8, 8), Image.NEAREST)
        
        # Convert to numpy array
        img_array = np.array(resized_img)
        
        # Initialize the grid
        grid = []
        
        for i in range(rows):
            row = []
            for j in range(cols):
                # Get the color of the current pixel (since the image is 8x8, each cell is one pixel)
                rgb_color = img_array[i, j].tolist()
                hsv_color = self.rgb_to_hsv(*rgb_color)
                row.append(hsv_color)
            grid.append(row)
        
        return grid

    def rgb_to_hsv(self, r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        return (int(h*360), int(s*100), int(v*100))