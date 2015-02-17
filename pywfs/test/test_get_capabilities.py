from pywfs.commands.get_capabilities import process
import xmltodict

class Handler():

	def GetCapabilities(self):
		return [('test1', 1), ('test2', 2)]

def test_process():
	f = open('./resources/GetCapabilities.xml', 'r')
	assert process({}, {}) == xmltodict.parse(f.read())

def test_process_custom():
	assert process(Handler(), {}) == [('test1', 1), ('test2', 2)]