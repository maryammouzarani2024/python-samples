import justpy as jp

# this class is actually a layout class
class MenuBar(jp.QLayout):
    def __init__(self, **kwargs):
        #initialize the parent class first:
        super().__init__(**kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self,
                            show_if_above=True,
                            v_model="leftDrawerOpen"
                            , side="left", bordered=True)

        # adding menu items
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)

        # adding link items to the menu
        a_classe = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="home", href="/", classes=a_classe)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classe)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classe)
        jp.Br(a=qlist)

        btn = jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                      icon="menu", click=self.drawer_move, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def drawer_move(widget, msg):
        if widget.drawer.value:
            widget.drawer.value=False
        else:
            widget.drawer.value=True