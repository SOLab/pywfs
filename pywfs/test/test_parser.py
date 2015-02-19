from pywfs.parser import Parser
from collections import OrderedDict

class Handler:
  def GetCapabilities(self, params):
    return OrderedDict([('test1', 1), ('test2', 2)])

  def GetFeature(self, params):
    return OrderedDict([('test1', 1), ('test2', 2)])


class Handler2:
  def GetCapabilities(self, params):
    return [('test1', 1), ('test2', 2)]

test_environ_get_feature = {
  'pydap.response': 'wfs',
  'SCRIPT_NAME': '',
  'REQUEST_METHOD': 'GET',
  'PATH_INFO': '/gfs.t00z.master.grbf03.10m.uv.grib2.wfs',
  'SERVER_PROTOCOL': 'HTTP/1.1',
  'QUERY_STRING': 'service=WFS&version=1.1.0&request=GetFeature&layer=UGRD_P0_L103_GLL0,VGRD_P0_L103_GLL0&srsname=EPSG:3413&outputFormat=jsonp&bbox=-1489257.8125,-2707519.53125,5000000,3020019.53125&resolution=4882.8125'
}

test_environ_get_capabilities = {
  'pydap.response': 'wfs',
  'SCRIPT_NAME': '',
  'REQUEST_METHOD': 'GET',
  'PATH_INFO': '/gfs.t00z.master.grbf03.10m.uv.grib2.wfs',
  'SERVER_PROTOCOL': 'HTTP/1.1',
  'QUERY_STRING': 'service=WFS&version=1.1.0&request=GetCapabilities'
}

def test_get_capabilities():
  parser_inst = Parser(Handler())
  assert parser_inst.process_request(test_environ_get_capabilities) == {
    'content_type': 'application/json',
    'data': '{"test1": 1, "test2": 2}'
  }

def test_get_feature_default():
  parser_inst = Parser(Handler())
  assert parser_inst.process_request(test_environ_get_feature) == {
    'content_type': 'application/json',
    'data': '{"test1": 1, "test2": 2}'
  }

def test_get_feature():
  parser_inst = Parser(Handler2())
  assert parser_inst.process_request(test_environ_get_feature) == {
    'content_type': 'application/json',
    'data': '{}'
  }