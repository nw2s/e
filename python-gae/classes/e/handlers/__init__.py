
from classes.config import config

def getLocale(webapp) :
	
	hostname = webapp.request.headers["Host"]
	domainmap = config["e"]["localization"]["domainmap"]

	return domainmap.get(hostname, domainmap["*"])
