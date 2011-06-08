
from django.utils import simplejson
from google.appengine.api import users

class defaultcommand():
   def run(self, requesthandler, method, content):

        template_values = {
			"content" : content
        }

	return template_values