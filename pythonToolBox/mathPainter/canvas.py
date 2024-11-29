import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width=width
        self.height=height
        self.color=color
        self.data=np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:]=self.color

    def make(self, imagepath):
        self.img=Image.fromarray(self.data, 'RGB')
        self.img.save(imagepath)


