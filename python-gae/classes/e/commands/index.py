

class index():
	def run(self, requesthandler, method, content):

		request = requesthandler.request

		template_values = {
			"content" : content
		}

		return template_values
				
		
