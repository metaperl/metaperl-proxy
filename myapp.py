# imports
## core

import importlib
import logging
import os
import pprint
import sys
import StringIO

## 3rd party
import cherrypy
sys.path.insert(0, "/home/schemelab/prg/meld3")
import meld3

## local
def full_path(*extra):
    return os.path.join(os.path.dirname(__file__), *extra)
sys.path.insert(0, full_path())

import db

logging.basicConfig()

class Root(object):

    @cherrypy.expose
    def index(self, tag):
        url = db.urls[tag]
        raise cherrypy.HTTPRedirect("http://www.duckduckgo.com")
