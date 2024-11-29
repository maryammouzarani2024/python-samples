import justpy as jp

from webapp.homepage import Home
from webapp.aboutpage import About
from webapp.dictionarypage import DictionaryPage


# adding the Routes dynamically:

imports= list(globals().values())

for obj in imports:
    if hasattr(obj, "path") and hasattr(obj, "serve"):
        jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(DictionaryPage.path, DictionaryPage.serve)

jp.justpy(port=8001)