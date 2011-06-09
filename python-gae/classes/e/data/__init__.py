import logging

from classes.config import config

from classes.e.data.xmlcontent import getContentForPage as getXMLContentForPage
from classes.e.data.jsoncontent import getContentForPage as getJSONContentForPage


def getContentProvider() :

	contentProviders = {
		"xmlcontent" : getXMLContentForPage,
		"jsoncontent" : getJSONContentForPage	
	}

	return contentProviders[config["e"]["content"]["module"]]
				
				
def getContentForPage(pagename, handler) :

	# get the concrete content provider
	getContentForPage_instance = getContentProvider()

	# get the locale
	locale = getLocale(handler) if config["e"]["content"]["localized"] else None

	return getContentForPage_instance(pagename, config["e"]["content"]["config"], locale)
	
	
def getLocale(handler) :
	
	hostname = handler.request.headers["Host"]
	domainmap = config["e"]["localization"]["domainmap"]

	return domainmap.get(hostname, domainmap["*"])
