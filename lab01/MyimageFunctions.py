# import numpy as np

# def myImageInverse(inImage):
#     """Return the image inverse (255 - value) of a grayscale numpy matrix."""
#     # Determine the size of the input matrix
#     rows, cols = inImage.shape
 
#     # Create a new matrix of the same size
#     outImage = np.zeros((rows, cols), dtype=np.uint8)
 
#     # Nested for loops to compute the inverse
#     for r in range(rows):
#         for c in range(cols):
#             in_value = int(inImage[r, c])
#             outImage[r, c] = 255 - in_value
 
#     return outImage
 