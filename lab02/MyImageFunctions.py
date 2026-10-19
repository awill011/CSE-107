
import numpy as np 

def mybilinear(x1, x2, y1, y2, v11, v12, v21, v22, x, y):


    if x2 == x1 or y2 == y1:
        if x1 == x2 and y1 == y2:
            return v11
        if x1 == x2: return y
        if y1 == y2: return x
    
    #interpolate along the y in the top row
    top = v11 +(v12 -v11) * (y-y1)/ (y2-y1)
   #along the y in the bottem row 
    bottom = v21 + (v22 - v21) * (y -y1)/ (y2- y1)
    #interpolat between thoose two results along x 
    value = top + bottom - top  *(x-x1)/ (x2-x1)

    return value

def myRMSE(i1,i2):

    


def myimResize(in_pixels, out_rows, out_cols, method):

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
            elif method == 'bilinear': #4 integer pixel locations
                x1 = min(max(int(np.floor(x)), 0 ), in_rows -1)
                x2 = min( x1+ 1, in_rows -1)
                y1 = min(max(int (np.floor(y)),0), in_cols -1)
                y2 = min(y1+1, in_cols-1)

                #so edge pixels dont extrapolate beyon the image
                xi = min(max(x,0), in_rows -1)
                yi = min(max(y,0), in_cols -1)
                #pixel values at the 4 neightbors 
                v11 = in_pixels[x1,y1]
                v12 = in_pixels[x1,y2]
                v21 = in_pixels[x2,y1]
                v22 = in_pixels[x2,y2]

                out_pixels[r, c] = mybilinear(x1, x2, y1, y2,
                                              v11, v12, v21, v22, xi, yi)

            else:
                raise ValueError("method must be 'nearest' or 'bilinear'")

    return out_pixels




            









