"""The Foodshed App"""

from bobo import Application
from google.appengine.ext.webapp import util


def main():
        util.run_wsgi_app(Application(bobo_resources='foodshed'))


if __name__ == '__main__':
    main()
