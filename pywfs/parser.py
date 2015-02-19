from paste.request import construct_url, parse_dict_querystring
import pywfs.commands.get_capabilities as get_capabilities
import pywfs.commands.get_feature as get_feature
from pywfs.serializers import serialize_json


class Parser:

  def __init__(self, handler):
    self.handler = handler

  def _checkVersion(self, query):
    if(query['version'] != '1.1.0'):
      raise Exception('We support only version 1.1.0')

  def select_command(self, query):
    if(not query.has_key('request')):
      raise Exception('request parameter is not specified')
    command = query['request']

    available_commands = {
      'GetCapabilities': get_capabilities.process,
      'GetFeature': get_feature.process
    }

    if(available_commands.has_key(command)):
      return available_commands[command]
    else:
      raise Exception('We do not support request %s', command)

  def process_request(self, query):
    parsed_query = parse_dict_querystring(query)
    self._checkVersion(parsed_query)
    command = self.select_command(parsed_query)
    response = {}
    data = command(self.handler, parsed_query)
    response['data'] = serialize_json(data)
    response['content_type'] = 'application/json'
    return response
