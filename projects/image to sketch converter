'''This python document help you to convert a colourful image to a black and white image. 
For this you need a numpy module, an imageio module, a scipy module and a cv2 module.

Also you need a latest version of python.

Try to have a face photograph, so that you can eaily observe the changes. Save it with the name Photo.jpg in the same directory.

A new image with extension .png and name Photo will be created in the same folder'''


import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "Photo.jpg"

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    
def dodge(front,back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')
    
s = imageio.imread(img)
g = grayscale(s)
i = 255-g

b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r = dodge(b,g)

cv2.imwrite('Photo.png',r)
