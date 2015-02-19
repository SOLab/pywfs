import json
from collections import OrderedDict

def serialize_json(data):
  print(isinstance(data, OrderedDict))
  if(isinstance(data, OrderedDict)):
    data = dict(data)
  return json.dumps(data)