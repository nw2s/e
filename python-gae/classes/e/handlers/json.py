import cgi

from google.appengine.ext import webapp
from django.utils import simplejson

from classes.e.commands import getCommand
from classes.e.data import getContentForPage
from classes.e.model.dictionarymodel import DictionaryModel

class JSONHandler(webapp.RequestHandler):

	def get(self, pagename):
		self.buildResponse(pagename, "GET")

	def post(self, pagename):
		self.buildResponse(pagename, "POST")

	def buildResponse(self, commandname, method):

		# set json mime type
		if self.request.get('nomime') != '1':
			self.response.headers['Content-Type'] = 'application/json; charset=utf-8'

		# get page content
		content = getContentForPage(commandname, self)
				
		# get command and run
		commandclass = getCommand(commandname)
		command = commandclass()
		result = command.run(self, method, content)

		# prep for serialization
		preppedobj = self.prepModelObj(result)		

		# serialize
		jsonstring = simplejson.dumps(preppedobj)
		
		# render
		self.response.out.write(cgi.escape(jsonstring))

	
	def prepModelObj(self, modelobj):
		
		# ensures that collections, objects, and dictionaries are json serializable
		if isinstance(modelobj, DictionaryModel):
			return modelobj.to_dict()
		elif isinstance(modelobj, basestring):
			return modelobj
		elif isinstance(modelobj, dict):
			return dict([(self.prepModelObj(key), self.prepModelObj(modelobj.get(key))) for key in modelobj.keys()])
		elif hasattr(modelobj, "__len__"):
			return map(self.prepModelObj, modelobj)
		else:
			return modelobj
					
	