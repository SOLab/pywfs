from collections import OrderedDict

def process(app, query):
  if(hasattr(app, 'GetFeature')):
    return app.GetFeature(query)
  else:
    return OrderedDict()