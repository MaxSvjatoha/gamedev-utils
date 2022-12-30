# A file meant to be used for testing the functionality of the various modules in the project

from functions.tile_colormap_settings import *
from functions.tile_generator import *
from functions.noise_funcs import *

import sys
import os

if __name__ == '__main__':
    
    print("starting script")
    
    colors = [(0, 102, 0), (0, 153, 0), (0, 204, 0), (0, 255, 0)]
    probabilities = [0.2, 0.3, 0.3, 0.2]
    noise_field = np.random.normal(0.3, 0.1, size=(256, 256))
    noise_field = np.clip(noise_field, 0, 1)
    generate_tile(size=(256, 256), colors=colors, probabilities=probabilities, noise_field=noise_field, show_tile=True, save=True, save_name="tile.png")
    
    sys.exit()
    
    # Load the tile colormap settings
    tile_types = []
    for tile_type in colormaps:
        tile_types.append(tile_type)
    
    for tile_type in tile_types:
        for i in range(60):
            
            # Check if save directory is valid. If not, create it
            if not os.path.isdir(f"./images/{tile_type}"):
                print(f"Creating directory: ./images/{tile_type}")
                os.mkdir(f"./images/{tile_type}")
            
            # Generate a tile
            generate_tile(size=tile_size, colors=colormaps[tile_type]["colors"], probabilities=colormaps[tile_type]["probabilities"], show_tile=False, save=True, save_name=f"./images/{tile_type}/{tile_type}_"+str(i)+".png")
            
'''
Some tile colormap ideas:

A "desert" tile:
colors = [(255, 255, 153), (255, 255, 204), (255, 255, 255)]
probabilities = [0.5, 0.3, 0.2]
noise_field = np.random.normal(0.5, 0.1, size=(256, 256))

A "snowy mountain" tile:
colors = [(204, 255, 255), (255, 255, 255), (255, 204, 204), (255, 153, 153)]
probabilities = [0.3, 0.3, 0.2, 0.2]
noise_field = np.random.normal(0.7, 0.1, size=(256, 256))

A "jungle" tile:
colors = [(0, 102, 0), (0, 153, 0), (0, 204, 0), (0, 255, 0)]
probabilities = [0.2, 0.3, 0.3, 0.2]
noise_field = np.random.normal(0.3, 0.1, size=(256, 256))

A "swamp" tile:
colors = [(102, 51, 0), (153, 76, 0), (204, 102, 0)]
probabilities = [0.3, 0.4, 0.3]
noise_field = np.random.normal(0.5, 0.1, size=(256, 256))

A "beach" tile:
colors = [(255, 255, 153), (255, 255, 204), (255, 255, 255)]
probabilities = [0.5, 0.3, 0.2]
noise_field = np.random.normal(0.2, 0.1, size=(256, 256))

A "frosty mountain" tile:
colors = [(51, 153, 255), (102, 204, 255), (153, 255, 255), (204, 255, 255)]
probabilities = [0.2, 0.3, 0.3, 0.2]
noise_field = np.random.normal(0.7, 0.1, size=(256, 256))

A "grassy" tile:
colors = [(0, 102, 0), (0, 153, 0), (0, 204, 0), (0, 255, 0)]
probabilities = [0.2, 0.3, 0.3, 0.2]
noise_field = np.random.normal(0.3, 0.1, size=(256, 256))

Some recipe storage ideas:
import json

tile_recipe = {
    "size": [256, 256],
    "colors": [[85, 85, 85], [110, 110, 110], [192, 192, 192], [60, 60, 60]],
    "probabilities": [0.3, 0.3, 0.3, 0.1],
    "noise_field": noise_field.tolist()
}

# writing to JSON file
with open("tiles.json", "w") as f:
    json.dump(tile_recipe, f)
    
# reading from JSON file
with open("tiles.json", "r") as f:
    tile_recipe = json.load(f)
'''