
import numpy as np 

def myImageResize(in_pixels, out_rows, out_cols, method):

    """ functions should resize a grayscale imaes using nearest neighbor or bilinear interpolation"""

    #determine the dimensions of the input matrcis 
    in_rows, in_cols = in_pixels.shape

    #create output matrix
    out_pixels = np.zeros((out_rows, out_cols), dtype = np.float32)

    #add rations of inpute size to output size

    row_scale = in_rows/out_rows
    col_scale = in_cols/ out_cols


    #look at every oixels in the output image

    for r in range(out_rows):
        for c in range(out_cols):
            #fins the non integer location in the input
            x = (r + 0.5) * row_scale - 0.5 #row location
            y = (c+ 0.5)* col_scale -0.5 #col location in input

            if method == 'nearest':
                #round to closest input pixel and clamp to image 
                xn = min(max(int(round(x)), 0),in_rows -1)
                yn = min(max(int(round(y)), 0), in_cols -1)
                out_pixels[r,c] = in_pixels[xn, yn]
            elif method == 'bilinear':
                x1 = min(max(int(np.floor(x)), 0 ), in_rows -1)
                x2 = min( x1+ 1, in_rows -1)
                y1 = min(max(int (np.floor(y)),0), in_cols -1)
                y2 = min(y1+1, in_cols-1)
                








