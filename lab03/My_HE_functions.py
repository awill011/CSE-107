# MyHEFunctions.py

# Import numpy
import numpy as np
import matplotlib.pyplot as plt

def compute_histogram( image_pixels ):
    #computes the normalized histogram of a gray scale image

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
 #takes a numpy matrix representing a grayscale image as imput and out pus a numpy matrix-equalized version of a image "    

 hist = compute_histogram(image_pixels) #normalized histogram for input image
 
 T = np.zeros(shape= (256)) #look up table for transformation T 

 L = 256
 cumulative = 0.0

 for k in range (L):
    cumulative += hist [k]  #sum of the histogram up to the level k 
    T[k] = (L-1)*cumulative #scale to range 0-255
 T = np.round(T)

 #plot the transformation
 plt.figure()
 plt.plot(range(L), T)
 plt.title('histogram equilization transformation')
 plt.xlabel('Input value')
 plt.ylabel('output pixel value')
 plt.xlim([0,255])
 plt.ylim([0,255])
 plt.grid(True)
 plt.show()     #close the window 

 M,N = image_pixels.shape
 eqalized_image = np.zeros(shape=(M,N), dtype = np.float32) #3 output is same as input
  
for m in range(M):
   for n in range(N):
        equalized_image[m][n] = T[int(image_pixels[m][n])]


return equalized_image
      




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
