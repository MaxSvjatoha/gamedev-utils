# A file meant to be used for testing the functionality of the various modules in the project

from functions.tile_colormap_settings import *
from functions.tile_generator import *

import sys
import os

if __name__ == '__main__':
    
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