# src/screen_reader/screen_capture.py

import mss
import numpy as np
from PIL import Image
import colorsys

class ScreenCapture:
    def __init__(self, x, y, width, height):
        self.bbox = {'top': y, 'left': x, 'width': width, 'height': height}
        self.sct = mss.mss()
        self.box_size = width // 8  # Assuming width is divisible by 8

    def capture(self):
        sct_img = self.sct.grab(self.bbox)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        return img

    def get_grid(self):
        img = self.capture()
        img_array = np.array(img)

        grid = []
        for i in range(8):
            row = []
            for j in range(8):
                top = i * self.box_size
                left = j * self.box_size

                cell = img_array[top+15:top+self.box_size-15, left+15:left+self.box_size-15]
                mask = np.ones_like(cell[:,:,0], dtype=bool)
                mask[25:65, 25:65] = False

                avg_color = np.mean(cell[mask], axis=0)
                hsv_color = self.rgb_to_hsv(*avg_color)
                row.append(hsv_color)
            grid.append(row)

        return grid

    @staticmethod
    def rgb_to_hsv(r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        return (int(h*360), int(s*100), int(v*100))