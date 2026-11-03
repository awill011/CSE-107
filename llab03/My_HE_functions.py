# MyHEFunctions.py

# Import numpy
import numpy as np

def compute_histogram( image_pixels ):
    "computes the normalized histogram of a gray scale image"

    #get the ima dimensions 
    M,N = image_pixels.shape
    hist = np.zeros(shape = 256)
    #loop every pixel and add oone to the bin that matc hes its vale
    for m in range(N):
        for n in range(N):
            hist[int(image_pixels[m][n])] += 1
    #divide the counts by the total number of pixels 
    hist = hist / (M*N)

    return hist

def equalize( in_image_pixels ):
"histogram equalization to a grayscale image and plots the transformation used to do it."
<your function header>

<your implementation>

def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     10/18/2026   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value');

    plt.ylabel('PMF'); 

    plt.show()
