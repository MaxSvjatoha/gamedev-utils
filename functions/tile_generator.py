import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union

def generate_tile(size: Tuple[int, int] = None, colors: Union[Tuple[int, int, int], List[Tuple[int, int, int]]] = None, probabilities: List[float] = None, noise_field: np.ndarray = None, show_tile: bool = False, save: bool = False, save_name: Union[str, None] = None) -> np.ndarray:
    """
    Generate a random tile with the specified size and colors using the specified probabilities and noise field.
    
    Parameters:
    size (tuple): The size of the tile (rows, columns).
    colors (list): A list of RGB tuples representing the colors to use.
    probabilities (list): A list of probabilities corresponding to the colors, in the same order.
    noise_field (np.ndarray): A 2D numpy array with values in the range 0-1 to use as the source of randomness.
    show_tile (bool, optional): Indicates whether the generated image should be displayed using Matplotlib's `imshow` function. The default value is `False`.
    save (bool, optional): Indicates whether the generated image should be saved to a file. The default value is `False`.
    save_name (str or None, optional): The name of the file to save the image to. If not specified, the image will be saved as "images/tile.png".
    
    Returns:
    np.ndarray: A 2D numpy array with shape (size[0], size[1], 3) representing the generated tile.
    
    Examples:
    Generate and return a basic 256x256 RGB tile:
    >>> tile =  generate_tile(size = (256, 256), colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)], probabilities = [0.5, 0.3, 0.2], noise_field = np.random.random((10, 10)), show_tile = True)
    """
    
    # Error checks
    # Size
    if size is None:
        raise ValueError("A size is required and none was specified.")
    if size.shape != (2,):
        raise ValueError("The size must be a tuple of length 2.")
    if size[0] <= 0 or size[1] <= 0:
        raise ValueError("The size must be greater than 0 in both dimensions.")
    if not isinstance(size[0], int) or not isinstance(size[1], int):
        raise ValueError("The size must be a tuple of integers.")
    # Colors and probabilities
    if colors is None or probabilities is None:
        raise ValueError(f"Both colors and probabilities are required and at least one was not specified. Colors: {colors}, Probabilities: {probabilities}.")
    if len(colors) != len(probabilities):
        raise ValueError("The number of colors and probabilities must match.")
    if sum(probabilities) != 1:
        raise ValueError("The probabilities must sum to 1.")
    if not (np.all(np.array(probabilities) >= 0) and np.all(np.array(probabilities) <= 1)):
        raise ValueError("The probabilities values must be in the range 0-1.")
    # Noise field
    if noise_field is None:
        raise ValueError("A noise field is required and none was specified.")
    if noise_field.ndim != 2:
        raise ValueError("The noise field must be 2D.")
    if noise_field.shape != size:
        raise ValueError("The noise field must be the same size as the tile.")
    if not (np.all(noise_field >= 0) and np.all(noise_field <= 1)):
        raise ValueError("The noise field must be in the range 0-1.")
    
    # Initialize the tile as a 3D array of zeros
    tile = np.zeros(size + (3,))
    # Initialize the color to the first color in the list
    color = colors[0]
    
    for i, j in np.ndindex(noise_field.shape):
        # Use the value at position (i, j) in the noise field as the probability
        r = noise_field[i, j]
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
        
    # Display the tile
    if show_tile:
        plt.imshow(tile)
        plt.show()   
    # Save the tile as an image file
    if save:
        if save_name == None:
            plt.imsave("images/tile.png", tile)
        else:
            plt.imsave(save_name, tile)
    return tile


def generate_sample_grid(size: Tuple[int, int], colors: Union[Tuple[int, int, int], List[Tuple[int, int, int]]], probabilities: List[float], save: bool = False, save_name: Union[str, None] = None) -> None:
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
    
    Example:
    >>> size = (16, 16)  # The size of the tiles (16x16 pixels)
    >>> colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # A list of 3 RGB tuples representing red, green, and blue
    >>> probabilities = [0.3, 0.4, 0.3]  # The probabilities associated with each color
    >>> generate_sample_grid(size, colors, probabilities, save=True, save_name="sample_grid.png")
    """
    # Convert colors to a list if it is a single tuple
    if isinstance(colors, tuple):
        colors = [colors]
    # Check that there is an associated probability for each color
    assert len(colors) == len(probabilities), "The number of colors and probabilities must match."
    
    # Generate 16 random tiles
    tiles = [generate_tile(size, colors, probabilities) for _ in range(16)]
    # Set up a 4x4 grid of subplots
    fig, axs = plt.subplots(4, 4, figsize=(10, 10))

    # Iterate through the subplots and tiles
    for ax, tile in zip(axs.flat, tiles):
        # Display the tile in the current subplot
        ax.imshow(tile / 255) # Rescale the pixel values to be between 0 and 1, necessary for imshow
        # Remove the axis labels
        ax.set_xticks([])
        ax.set_yticks([])
        
    # Remove the space between subplots (optional, function will still work without this)
    plt.subplots_adjust(wspace=0, hspace=0)
        
    # Save the plot as an image file
    if save:
        if save_name == None:
            plt.savefig("tile_colormap.png")
        else:
            plt.savefig(save_name)
            
    # Show the plot
    plt.show()
    plt.close(fig)
    
# Test generate_tile using its example
if __name__ == '__main__':
    
    # TODO: fix AttributeError: 'tuple' object has no attribute 'shape' (line 30, if size.shape != (2,):)
    generate_tile(size=(256, 256), colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255)], probabilities=[0.5, 0.3, 0.2], show_tile=True)