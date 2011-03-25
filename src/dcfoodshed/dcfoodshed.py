from google.appengine.api import users
from google.appengine.ext import db

import bobo
import chameleon.zpt.loader
import os


template_path = os.path.join(os.path.dirname(__file__), 'templates')

template_loader = chameleon.zpt.loader.TemplateLoader(
        template_path,
        auto_reload=os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'))
        
master = template_loader.load('master.html')

@bobo.query('/')
def index():
    template = template_loader.load('index.html')
    return template(master=master)
