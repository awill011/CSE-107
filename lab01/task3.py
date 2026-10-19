# from PIL import Image
# import numpy as np 
# import matplotlib.pyplot as plt

# rows = 100
# cols = 256
# #100x256 grayscale image -0 to the left to 256 to the  right

# gradient = np.zeros((rows, cols), dtype=np.uint8)
# for r in range (rows):
#     for c in range(cols):
#         gradient[r,c]= c

# #display image

# plt.imshow(gradient, cmap= 'gray',vmin =0, vmax =255)
# plt.title('Gradient image')
# plt.axis('off')
# plt.show()

# #save as a tiff
# Image.fromarray(gradient).save('gradient.tif')

# #compute average  pixel value

# total = 0
# for r in range(rows):
#     for c in range(cols):
#         total += int (gradient[r,c])
# average = total/(rows *cols)
# print('average pixel value:', average)