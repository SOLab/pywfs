import json
from collections import OrderedDict
from json import JSONEncoder

class Serializer(JSONEncoder):
  def default(self, o):
    if(o.to_JSON):
      return o.to_JSON()
    return o

def serialize_json(data):
  if(isinstance(data, OrderedDict)):
    data = dict(data)
  return json.dumps(data, cls=Serializer)