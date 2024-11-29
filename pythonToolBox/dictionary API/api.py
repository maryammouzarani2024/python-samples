from http.client import responses

import justpy as jp
import json


import definition

class Api:

    @classmethod
    def serve(cls, req):
        #we need wp to handle the users requests
        wp=jp.WebPage()
        query_param=req.query_params.get('w')
        word=definition.Definition(query_param).get()
        """ With the below code we add div and many html constructions to the response
        which are not necessary, for the api we require a simple text or json response
        so instead, we add the word to the html property of the page.
            
        """
        #jp.Div(a=wp, text=word.title()) #write the word with first capitalized letter
        #lets make it standard and write the result into a json dictionary
        #wp.html=word
        response={
            "word": query_param,
            "definition": word
        }

        wp.html=json.dumps(response)
        return  wp
