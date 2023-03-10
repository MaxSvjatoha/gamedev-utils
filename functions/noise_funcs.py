import numpy as np
from scipy.ndimage import zoom
from typing import Tuple
from matplotlib import pyplot as plt

import numpy as np
from typing import Tuple

import sys

def white_noise(shape: Tuple[int, int], input_range: Tuple[float, float] = (0, 1)) -> np.ndarray:
    """
    Generate white noise field using NumPy.
    
    Parameters
    ----------
    shape : tuple of ints
        The dimensions of the noise field.
    range : tuple of floats, optional
        The desired output range of the noise field. The default is (0, 1).
    
    Returns
    -------
    np.ndarray
        The generated white noise field.
        
    Examples
    --------
    Generate a 2D noise field in the range 0 to 1:
    
    >>> shape = (256, 256)
    >>> noise = white_noise(shape)
    
    Generate a 3D noise field in the range -1 to 1:
    
    >>> shape = (256, 256, 256)
    >>> noise = white_noise(shape, range=(-1, 1))
    """
    
    # Error checks
    # Input range
    assert input_range[0] < input_range[1], "The input range must be in the form (min, max)."
    assert input_range.shape == (2,), "The input range must be a tuple of length 2."
    assert isinstance(input_range[0], float) and isinstance(input_range[1], float), "The input range must be a tuple of floats."
    # Shape
    assert shape.shape == (2,), "The shape must be a tuple of length 2."
    assert shape[0] > 0 and shape[1] > 0, "The shape must be greater than 0 in both dimensions."
    assert isinstance(shape[0], int) and isinstance(shape[1], int), "The shape must be a tuple of integers."
    
    if range[0] == range[1]:
        return np.full(shape, range[0])
    
    # Generate random values in the desired range
    noise = np.random.uniform(*range, size=shape)
    return noise

def perlin_noise(shape: Tuple[int, int], scale: float = 1, octaves: int = 1, 
                 persistence: float = 0.5, lacunarity: float = 2) -> np.ndarray:
    """
    Generate Perlin noise field using NumPy.
    
    Parameters
    ----------
    shape : tuple of ints
        The dimensions of the noise field.
    scale : float, optional
        The range of the output noise field. The default is 1.
    octaves : int, optional
        The number of octaves of noise to add to the field. The default is 1.
    persistence : float, optional
        The decay of the amplitudes of successive octaves. The default is 0.5.
    lacunarity : float, optional
        The increase in frequency of successive octaves. The default is 2.
    
    Returns
    -------
    np.ndarray
        The generated Perlin noise field.
        
    Examples
    --------
    Generate a 2D noise field:
    
    >>> shape = (256, 256)
    >>> noise = perlin_noise(shape)
    
    Generate a 3D noise field:
    
    >>> shape = (256, 256, 256)
    >>> noise = perlin_noise(shape)
    
    Generate an RGB image:
    
    >>> import numpy as np
    
    >>> image = np.stack([perlin_noise(shape, scale=255) for _ in range(3)], axis=-1)
    >>> image = image.astype(np.uint8)
    
    """
    # Initialize the noise field with random values
    noise = np.random.rand(*shape)
    # Set the initial frequency and amplitude values
    frequency = 1
    amplitude = 1
    # Add octaves of noise to the field
    for _ in range(octaves):
        # Interpolate the noise field to the new frequency
        noise = np.interp(noise, (noise.min(), noise.max()), (0, 1))
        # Use the correct zoom factor for the dimensions of the noise field
        zoom_factor = (frequency,) * len(shape)
        noise = zoom(noise, zoom_factor, order=1)
        # Add the octave to the output field
        output = noise * amplitude
        # Update the frequency and amplitude values for the next octave
        frequency *= lacunarity
        amplitude *= persistence
    # Scale the output field to the desired range
    return output * scale