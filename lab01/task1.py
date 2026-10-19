# # Import pillow
# from PIL import Image, ImageOps

# # Import numpy
# import numpy as np
# from numpy import asarray

# # Read the image from file.
# im = Image.open('Beginnings.jpg')

# # Show the image.
# im.show()

# # Convert image to gray scale.
# im_gray = ImageOps.grayscale(im)

# # Show the grayscale image.
# im_gray.show()

# # Get access to the pixel values through the matrix im_gray_pixels.
# im_gray_pixels = asarray(im_gray)

# # Determine the dimensions of the image.
# rows, cols = im_gray_pixels.shape
# print("Image size is: ", rows, "rows x", cols, "columns")



# #max pixel value of the orginal grayscale image
# max_gray = 0
# for row in range (rows):
#     for col in range (cols):
#         if im_gray_pixels[row,col]>max_gray:
#             max_gray = im_gray_pixels[row,col]
# print("Max Pixel value of grayscale image: ", max_gray)

# #rotate 90 degreees

# #newmatrix is cols-1-col, row
# ccw_pixels = np.zeros(shape=(cols,rows))
# for row in range(rows):
#     for col in range(cols):
#         ccw_pixels[cols - 1 - col, row] = im_gray_pixels[row, col]

# #creat image from rotated matrix
# im_ccw =Image.fromarray(np.uint8(ccw_pixels))
# im_ccw.show()
# im_ccw.save("Beginnings_grayscale_ccw.jpg")



# #clockwise image

# cw_pixels= np.zeros(shape= (cols,rows))
# for row in range(rows):
#     for col in range(cols):
#         cw_pixels[col, rows - 1 - row] = im_gray_pixels[row, col]
# #create image
# im_cw=Image.fromarray(np.uint8(cw_pixels))
# im_cw.show()
# im_cw.save("Beginnings_grayscales_cw.jpg")


# #max pixel value of the orginal grayscale image
# cw_rows, cw_cols = cw_pixels.shape
# max_cw = 0
# for row in range(cw_rows):
#     for col in range(cw_cols):
#         if cw_pixels[row, col] > max_cw:
#             max_cw = cw_pixels[row, col]
# print("Max pixel value of clockwise rotated image:", max_cw)
