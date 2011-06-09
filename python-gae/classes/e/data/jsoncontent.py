import os
import logging

from django.utils import simplejson		
	
def getContentForPage(page, config, locale) :
	
	localesuffix = ("." + locale) if locale else ""
	
	filepath = os.path.join(os.path.dirname('.') + "data/content/" + page + localesuffix + ".json")
	
	logging.debug(filepath)
	
	return simplejson.load(open(filepath)) if os.path.isfile(filepath) else None
		
		