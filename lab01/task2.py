# import numpy as np 
# from PIL import Image
# from MyimageFunctions import myImageInverse

# #read/confirm grayscale
# im = Image.open("Tree.tif")

# print ("image mode is:", im.mode)

# #display
# im.show()
# #create  numpy matrix
# inMatrix = np.array(im)

# #make inverse using function from image function
# outMatrix = myImageInverse(inMatrix)

# #create an image from return matrix

# outIm = Image.fromarray(outMatrix, mode= "L")

# #displat image
# outIm.show()

# #write the inverse image to a .tif file

# outIm.save("TreeInverse.tif")


# print("Max pixel value of inverse image:", outMatrix.max())
# print("Min pixel value of original image:", inMatrix.min())
# print("Max pixel value of original image:", inMatrix.max())
 