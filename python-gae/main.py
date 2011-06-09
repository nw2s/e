import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from classes.config import config
from classes.e.handlers.html import HTMLHandler
from classes.e.handlers.json import JSONHandler

application = webapp.WSGIApplication(
                                     [('/services/([a-zA-Z/]+)', JSONHandler),
									  ('/([a-zA-z/]*)', HTMLHandler)],
                                     debug=False)

def main():
	logging.getLogger().setLevel(getattr(logging, config["e"]["logginglevel"]))
	run_wsgi_app(application)

if __name__ == "__main__":
    main()


