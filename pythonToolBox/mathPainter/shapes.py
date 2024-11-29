import numpy as np

class Rectangle:

    def __init__(self, x,y, width, height, color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.data=np.zeros((self.width, self.height,3), dtype=np.uint8)
        self.data[:]=self.color

    def draw(self, canvas):
        canvas.data[self.x:self.x+self.width, self.y:self.y+self.height ]=self.color


class Square:
    
    def __init__(self, x, y, side, color):
        self.x=x
        self.y=y
        self.side=side
        self.color=color 

    def draw(self, canvas):
        canvas.data[self.x: self.x+self.side, self.y:self.y+self.side  ]= self.color


