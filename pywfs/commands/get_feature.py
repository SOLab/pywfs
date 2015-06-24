from collections import OrderedDict

def process(app, query):
  if(hasattr(app, 'GetFeature')):
    ret = app.GetFeature(query)
    return ret
  else:
    return OrderedDict()