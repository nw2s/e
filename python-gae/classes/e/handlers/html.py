import os
import logging

import __main__ as main

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp

from classes.e.commands import getCommand
from classes.e.data import getContentForPage

class HTMLHandler(webapp.RequestHandler):

	def get(self, pagename):
		self.buildResponse(pagename, "GET")

	def post(self, pagename):
		self.buildResponse(pagename, "POST")

	def buildResponse(self, pagename, method):
		# todo - send 404 when no file found

		# default pagename is index
		if pagename == '' or pagename.endswith("/"): pagename += "index"

		# get the page content
		content = getContentForPage(pagename, self)

		# get the template_values from the command
		template_values = self.runCommand(pagename, method, content) if (pagename != None) else None

		# load the template for a given path and render it
		path = os.path.join(os.path.dirname(main.__file__), 'templates/pages/' + pagename + '.html')
		self.response.out.write(template.render(path, template_values))


	def runCommand(self, pagename, method, content):

		commandclass = getCommand(pagename)
		if commandclass == None: return None

		command = commandclass()
		return command.run(self, method, content)
		