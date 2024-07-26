import numpy as np
from sklearn.cluster import KMeans

# Define the centroids
centroids = np.array([
    [312, 24, 30],   # R
    [251, 40, 66],   # P
    [184, 74, 69],   # G
    [342, 22, 94],   # Y
    [211, 36, 82],   # B
    [17, 55, 96]     # O
])

# Create a KMeans model with the number of clusters equal to the number of centroids
kmeans = KMeans(n_clusters=len(centroids), init=centroids, n_init=1)

# Fit the model (formality)
kmeans.fit(centroids)

# Function to classify a new HSB value
def classify_color(h, s, b):
    hsb_value = np.array([[h, s, b]])
    cluster = kmeans.predict(hsb_value)[0]
    letter = ['R', 'P', 'G', 'Y', 'B', 'O'][cluster]
    return letter

# List of RGB values and expected classifications
rgb_values = [
    (255, 234, 249), (99, 77, 138), (105, 88, 150), (55, 249, 250), 
    (123, 75, 84), (104, 91, 156), (255, 175, 134), (50, 182, 183), 
    (94, 70, 87), (103, 81, 144), (108, 87, 152), (68, 37, 49), 
    (255, 160, 120), (98, 129, 172), (255, 229, 242), (47, 149, 152), 
    (111, 62, 133), (253, 151, 112), (248, 145, 105), (112, 146, 188), 
    (253, 216, 233), (97, 66, 67), (255, 160, 119), (255, 160, 122), 
    (51, 221, 222), (247, 192, 201), (54, 255, 255), (255, 209, 220), 
    (241, 137, 101), (92, 62, 65), (110, 139, 175), (30, 105, 110), 
    (97, 84, 81), (238, 136, 98), (237, 136, 98), (175, 214, 248), 
    (248, 175, 184), (254, 181, 191), (119, 148, 183), (111, 104, 166), 
    (87, 79, 79), (81, 74, 76), (238, 178, 189), (173, 212, 248), 
    (232, 156, 162), (132, 133, 197), (248, 155, 114), (114, 110, 175), 
    (160, 201, 236), (73, 66, 69), (52, 41, 51), (58, 213, 218), 
    (50, 160, 167), (227, 150, 160), (124, 122, 190), (241, 155, 117), 
    (175, 211, 248), (175, 210, 248), (254, 173, 185), (28, 24, 32), 
    (146, 176, 213), (40, 108, 117), (120, 145, 183), (26, 90, 98)
]

# Classify each RGB value and print the result
for rgb in rgb_values:
    h, s, v = rgb_to_hsb(*rgb)
    classified_letter = classify_color(h, s, v)
    print(f"RGB {rgb} -> HSB ({h:.2f}, {s:.2f}, {v:.2f}) -> Classified as: {classified_letter}")
