import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union

# Discovered good color combinations:
# Dirt: (180/255, 120/255, 50/255), (150/255, 100/255, 40/255), (120/255, 80/255, 30/255)
# Grass: (0/255, 255/255, 0/255), (0/255, 200/255, 0/255), (0/255, 150/255, 0/255)

size = (64, 64)
colors = [(180/255, 120/255, 50/255), (150/255, 100/255, 40/255), (120/255, 80/255, 30/255)]
probabilities = [0.1, 0.3, 0.6]

def generate_tile(size: Tuple[int, int], colors: Union[Tuple[int, int, int], List[Tuple[int, int, int]]], probabilities: List[float]) -> np.ndarray:
    """
    Generate a random tile with the specified size and colors using the specified probabilities.
    
    Parameters:
    size (tuple): The size of the tile (rows, columns).
    colors (list): A list of RGB tuples representing the colors to use.
    probabilities (list): A list of probabilities corresponding to the colors, in the same order.
    
    Returns:
    np.ndarray: A 2D numpy array with shape (size[0], size[1], 3) representing the generated tile.
    """ 
    tile = np.zeros(size + (3,))
    for i in range(size[0]):
        for j in range(size[1]):
            # Generate a random number between 0 and 1
            r = np.random.random()
            # Initialize the color to the first color in the list
            color = colors[0]
            # Iterate through the probabilities and colors
            for p, c in zip(probabilities, colors):
                # If the random number is less than the probability, set the color and break out of the loop
                if r < p:
                    color = c
                    break
                # Otherwise, subtract the probability from the random number and continue iterating
                r -= p
            # Set the pixel at position (i, j) to the chosen color
            tile[i, j] = color
    return tile


def generate_sample_grid(size: Tuple[int, int], colors: Union[Tuple[int, int, int], List[Tuple[int, int, int]]], probabilities: List[float], save: bool, save_name: Union[str, None] = None) -> None:
    """
    Generate a 4x4 grid of random tiles using the specified size, colors, and probabilities, and display or save it.
    
    Parameters:
    size (tuple): The size of the tiles (rows, columns).
    colors (tuple or list): An RGB tuple or a list of RGB tuples representing the colors to use.
    probabilities (list): A list of probabilities corresponding to the colors, in the same order.
    save (bool): Whether to save the plot as an image file.
    save_name (str, optional): The name of the image file to save. Defaults to None.
    
    Returns:
    None
    """
    # Convert colors to a list if it is a single tuple
    if isinstance(colors, tuple):
        colors = [colors]
    # Check that there is an associated probability for each color
    if len(colors) != len(probabilities):
        raise ValueError("Number of colors must match number of probabilities")
    # Generate 16 random tiles
    tiles = [generate_tile(size, colors, probabilities) for _ in range(16)]

    # Set up a 4x4 grid of subplots
    fig, axs = plt.subplots(4, 4, figsize=(10, 10))

    # Iterate through the subplots and tiles
    for ax, tile in zip(axs.flat, tiles):
        # Display the tile in the current subplot
        ax.imshow(tile)
        # Remove the axis labels
        ax.set_xticks([])
        ax.set_yticks([])
        
    # Save the plot as an image file
    if save:
        if save_name == None:
            plt.savefig("tile_colormap.png")
        else:
            plt.savefig(save_name)

    # Show the plot
    plt.show()
