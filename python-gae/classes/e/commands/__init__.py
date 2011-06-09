
#from classes.e.commands.default import defaultcommand

def getCommand(commandname):
	# todo: cache some of this so we don't do it every request???
	try:
		modulename = "classes.e.commands." + commandname.replace("/", ".")
		module = __import__(modulename)
		
		parts = modulename.split('.')
		classname = parts[-1]
		parts.append(classname)

		# if there is no module itself, then assume the page doesn't need a command.
		# maybe we need a default command instead?
		for part in parts[1:]:
			#if not hasattr(module, part): return defaultcommand
			if not hasattr(module, part): return None
			module = getattr(module, part)
		
		return module
	except ImportError:
		# log a note of this!
#		return defaultcommand
		return None