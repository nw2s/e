import os
import logging 

from xml.etree.ElementTree import ElementTree

def getContentForPage(page, config, locale) :

	# config:
	# collapsetextnodes: tells the parser not to use "text" fields, but to collapse the entire element into
	#                    { tag : text }. This will ignore any other attributes or child nodes if they exist. 
	#					 this is useful for xml that uses a lot of <tag>text</tag> structure.
	#

	collapsetextnodes = config["collapsetextnodes"]
	localesuffix = ("." + locale) if locale else ""

	# todo cache this stuff
	filepath = os.path.join(os.path.dirname('.') + "data/content/" + page + localesuffix + ".xml")
	
	if not os.path.isfile(filepath) : return None
	
	doc = ElementTree()
	doc.parse(filepath)
	root = doc.getroot()
	
	return parseXMLnode(root, collapsetextnodes)


def parseXMLnode(node, collapsetextnodes) :

	# set up an initial dictionary for this node with the current attributes
	nodevalues = dict([(attr, node.get(attr)) for attr in node.keys()]) if node.keys() else dict()

	# if this node has text, either add a new node or collapse it into this one.
	if not (node.text == None or len(node.text) == 0 or node.text.isspace()) :
		if collapsetextnodes : return node.text.strip()
		nodevalues.update({ "text" : node.text.strip() })
	
	# iterate over the child nodes recursively
	for child in node.getchildren() :
		# multiple nodes of the same tag are treated as an array
		if (isarrayelement(node, child.tag)) :
			if (nodevalues.has_key(child.tag)) :
				nodevalues[child.tag].append(parseXMLnode(child, collapsetextnodes))
			else :
				nodevalues[child.tag] = [ parseXMLnode(child, collapsetextnodes) ]
		else :
			nodevalues.update({ child.tag : parseXMLnode(child, collapsetextnodes) }) 

	return nodevalues


def isarrayelement(node, tag) :

	return len(node.findall(tag)) > 1		
	