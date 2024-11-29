import justpy as jp
from pandas.core.dtypes.common import classes
from webapp import navbar

class Home:
    path="/"
    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)
        #adding a menu to the web page:
        layout=navbar.MenuBar(a=wp, view="hHh LpR fFf")


        container=jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page.", classes="text-4xl m-2")
        jp.Div(a=div, text="""

                Self-improvement, as defined by Merriam-Webster, 
                is the act or process of improving oneself by one's own actions; 
                it is an instance or result of such improvement.
                 This improvement helps re-focus our lives and typically results in a positive change.
                """, classes="text-lg")
        return wp

