import random
from PIL import Image

# Define a function to generate a random tile of a given size and using a given set of colors and probabilities for each color
# Add independant options to print the tile to the console, saving the tile as an image or displaying the tile in a window.
def generate_tile(size, colors, probabilities, print_tile=False, save_tile=False, save_name=None, display_tile=False):
    # Create a list of the colors and probabilities
    color_list = []
    for i in range(len(colors)):
        color_list += [colors[i]] * probabilities[i]
    
    # Generate a random tile
    tile = []
    for i in range(size):
        tile.append([])
        for j in range(size):
            tile[i].append(random.choice(color_list))
    
    # Print the tile to the console
    if print_tile:
        for i in range(size):
            for j in range(size):
                print(tile[i][j], end=" ")
            print()
    
    # Save the tile as an image
    if save_tile:
        # Create a new image
        img = Image.new('RGB', (size, size))
        # Fill the image with the tile
        for i in range(size):
            for j in range(size):
                img.putpixel((i, j), tile[i][j])
        # Save the image
        if save_name == None:
            img.save("tile.png")
        else:
            img.save(save_name)
    
    # Display the tile in a window
    if display_tile:
        # Create a new image
        img = Image.new('RGB', (size, size))
        # Fill the image with the tile
        for i in range(size):
            for j in range(size):
                img.putpixel((i, j), tile[i][j])
        # Display the image
        img.show()
    
    # Return the tile
    return tile