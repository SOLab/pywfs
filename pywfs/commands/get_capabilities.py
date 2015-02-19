import xmltodict

def process(app, params):
	if hasattr(app, 'GetCapabilities'):
		return app.GetCapabilities(params)
	else:
		f = open('./resources/GetCapabilities.xml', 'r')
		return xmltodict.parse(f.read())