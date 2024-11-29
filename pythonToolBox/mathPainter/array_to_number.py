import numpy as np
from PIL import Image


data=np.zeros((5,4,3), dtype=np.uint8) # create a cube with 0 values it has 3 dimensions


#change the whole value of matrix 
data[:]=[255,255,0]

print(data)
#changing rows2 and 3
data[1:3]=[255,0,0]

#changing the columns

data[:, 1:3]=[0,255,0]

data[1:4, 1:3]=[1,1,1]
#create an image from the array of integer as RGB

img= Image.fromarray(data, 'RGB') # the data array defines the RGB values
img.save('canvas.png')
