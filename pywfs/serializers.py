import json
from collections import OrderedDict

def serialize_json(data):
  if(isinstance(data, OrderedDict)):
    data = dict(data)
  return json.dumps(data)