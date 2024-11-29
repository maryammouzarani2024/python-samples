
from canvas import Canvas
from shapes import Square, Rectangle

canvas_width= int(input("Enter canvas width:  "))
canvas_height=int(input("Enter canvas height: "))

colors={"white": (255,255,255), "black":(0,0,0)}
canvas_color= input("Enter canvas color (white or black): ")
canvas_color=canvas_color.lower()

canvas=Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    shape_type=input("Which shape you want to draw (rectangle or square)? Enter quit to quit ")
    if shape_type.lower()=="rectangle":
        rec_x=int(input("What is x of rectangle? "))
        rec_y=int(input("What is y of rectangle? "))
        rec_width=int(input("What is the width of rectangle? "))
        rec_height=int(input("What is the height if rectangle? "))
        red=int(input("How much red? "))
        green=int(input("How much green? "))
        blue=int(input("How much blue? "))

        r1=Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas=canvas)
    if shape_type.lower()=="square":
        sq_x=int(input("What is x of square? "))
        sq_y=int(input("What is y of square? "))
        sq_side=int(input("What is the side of square? "))
        red=int(input("How much red? "))
        green=int(input("How much green? "))
        blue=int(input("How much blue? "))

        s1=Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
        s1.draw(canvas=canvas)

    if shape_type=="quit":
        break

canvas.make('canvas.png')