import justpy as jp
import requests
import pandas

#import definition
from webapp import navbar
class DictionaryPage:
    path="/dictionary"

    """ in order to prevent the timing bomb problem with calling serve function without an instance, 
        we have to use a class method decorator to define serve function as to be called with the class
        and without the instance, in this way self would represent the class type, 
        otherwise, there would be no self value when the function is called with DictionaryPage.serve()
        and justpy call this function with a request object DictionaryPage.serve(requests) and that would
        wrongly consider self as a request object
    """
    @classmethod
    def serve(cls,req):
        #req to access the request obj

        wp = jp.QuasarPage(tailwind=True)
        layout=navbar.MenuBar(a=wp, view="hHh LpR fFf")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="Instant English Dictionary.", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-lg")

        result_box=jp.Div(a=div, classes="h-40 m-2 p-2 text-lg border-2 rounded border-gray-400")
        #lets make the behavior automatically as the user type in the text box
        """jp.Button(a=div, text="search", click=cls.search,
                  in1=input_box,in2=result_box,
                  classes="border border-blue-500 m-2 py-1 px-4 "
                          "rounded text-blue-600 hover:bg-red-500 "
                          "hover:text-white")"""

        input_box = jp.Input(a=div, placeholder="Type in a word here ...",
                             outputbox=result_box,
                             classes="m-2 rounded bg-gray-100 border-2 border-gray-200 "
                                     "focus:bg-white focus:border-red-500 focus:outline-none"
                                     "px-2 py-4 w-64 ")
        input_box.on('input', cls.search)
        return  wp

    #we define as a static method so that python does not call the function with the class instance or the class itself
    #it is like an independent method that has access to the class
    @staticmethod
    def search(widget, msg):
            #lets get it from our own api
            #result=definition.Definition(widget.value).get()
            result=requests.get(f" http://127.0.0.1:8000/api?w={widget.value}")
            data=result.json()
            widget.outputbox.text = " ".join(data['definition']) #Join all items in a tuple into a string

