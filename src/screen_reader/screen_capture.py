import mss
import numpy as np
from PIL import Image

class ScreenCapture:
    def __init__(self, x, y, width, height):
        self.bbox = {'top': y, 'left': x, 'width': width, 'height': height}
        self.sct = mss.mss()

    def capture(self):
        # Capture the specified area of the screen
        sct_img = self.sct.grab(self.bbox)
        # Convert to PIL Image
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
        # Resize the image to 8x8 pixels without any processing
        img = img.resize((8, 8), Image.NEAREST)
        return img

    def get_grid(self, rows=8, cols=8):
        # Capture the screen and resize to 8x8
        img = self.capture()
        # Convert to numpy array
        img_array = np.array(img)
        
        # Initialize the grid
        grid = []
        
        for i in range(rows):
            row = []
            for j in range(cols):
                # Get the color of the current pixel (since the image is 8x8, each cell is one pixel)
                color = img_array[i, j].tolist()
                row.append(color)
            grid.append(row)
        
        return grid
