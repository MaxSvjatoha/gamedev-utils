# A file meant to be used for testing the functionality of the various modules in the project

from functions.tile_colormap_generator import *

if __name__ == '__main__':
    
    for i in range(10):
        generate_tile(size=(64, 64), colors=colormaps["grass"]["colors"], probabilities=colormaps["grass"]["probabilities"], show_tile=False, save=True, save_name="dirt_test_"+str(i)+".png")