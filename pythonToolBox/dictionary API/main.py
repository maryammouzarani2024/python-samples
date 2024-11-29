import documenatation
import api

import justpy as jp


jp.Route("/", documenatation.Doc.serve)
jp.Route("/api", api.Api.serve)
jp.justpy()