import justpy as jp
from pandas.core.dtypes.common import classes


#map the function into a url path using a function decorator:
@jp.SetRoute("/")
def home():
    wp=jp.QuasarPage(tailwind=True  )
    #to add styling use the very easy tailwindcss styling method as the classes argument
    div=jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1=jp.Div(a=div, classes="grid grid-col-3 gap-4 p-3")
    in_1= jp.Input(a=div1, placeholder="Enter first value",
             classes="form-input")
    in_2= jp.Input(a=div1, placeholder="Enter Second Value",
             classes="form-input")
    d_output=jp.Div(a=div1, text="Results go here...")


    div2=jp.Div(a=div, classes="grid grid-col-3 gap-4 p-3")
    jp.Button(a=div2, text="Calculate",  click=sum_up,in1= in_1, in2= in_2,
              d=d_output,
              classes="border border-blue-500 m-2 py-1 px-4 "
                      "rounded text-blue-600 hover:bg-red-500 "
                      "hover:text-white")

    jp.Div(a=div2, text="I am a cool interactive div",
           classes="hover:bg-red-500", mouseenter=mouse_enter,
           mouseleave=mouse_leave)
    return wp



#creating another page:
@jp.SetRoute("/about")
def home():
    wp=jp.WebPage()
    jp.Div(a=wp, text="hi World!")
    jp.Div(a=wp, text="hi again!")
    return wp


def sum_up(widget, msg):
    print("Clicked!!!!")
    output=(float(widget.in1.value)+ float(widget.in2.value))
    widget.d.text=output
#map the function to a url path:
#jp.Route("/", home)
#we can also use a python decorator
def mouse_enter(widget, msg):
    widget.text="Mouse entered the house!"


def mouse_leave(widget, msg):
    widget.text = "Mouse left the house!"


#running the app
jp.justpy()
