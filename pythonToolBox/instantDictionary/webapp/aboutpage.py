import justpy as jp
from pandas.core.dtypes.common import classes

from webapp import navbar
class About:
    """
    When 10 users visit our about web page 10 instance of
    this class is instantiated.
    """

    path="/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        layout=navbar.MenuBar(a=wp, view="hHh LpR fFf")

        """
        The quasar page is responsible for html and design of the page
        and About class is responsible for the url and handling the user's behavior.
        """
        container=jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")

        jp.Div(a=div, text="This is the about page.", classes=" p-2 text-4xl m-2")
        jp.Div(a=div, text="""
        
        Self-improvement, as defined by Merriam-Webster, 
        is the act or process of improving oneself by one's own actions; 
        it is an instance or result of such improvement.
         This improvement helps re-focus our lives and typically results in a positive change.
        """, classes="text-lg")
        return wp

