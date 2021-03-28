import json
from pprint import pprint

with open('data.json') as f:
    data = str(json.load(f))
    print data

pprint (data)
