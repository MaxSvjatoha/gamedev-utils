# Tile size
tile_size = (64, 64)

# Tile colormap settings
colormaps = {
            "dirt": {"colors": [(180/255, 120/255, 50/255), (150/255, 100/255, 40/255), (120/255, 80/255, 30/255)], "probabilities": [0.1, 0.3, 0.6]},
            "grass": {"colors": [(120/255, 80/255, 30/255), (150/255, 100/255, 40/255), (0/255, 200/255, 0/255), (0/255, 150/255, 0/255)], "probabilities": [0.1, 0.15, 0.25, 0.5]},
            "water": {"colors": [(0/255, 0/255, 255/255), (0/255, 0/255, 200/255), (0/255, 0/255, 150/255)], "probabilities": [0.1, 0.3, 0.6]},
            "sand": {"colors": [(255/255, 255/255, 0/255), (200/255, 200/255, 0/255), (150/255, 150/255, 0/255)], "probabilities": [0.1, 0.3, 0.6]},
            "stone": {"colors": [(100/255, 100/255, 100/255), (80/255, 80/255, 80/255), (60/255, 60/255, 60/255)], "probabilities": [0.1, 0.3, 0.6]},
            }