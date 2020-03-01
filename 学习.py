import json
data = {'id':3, 'name':'ruiqiu','pwd':'2233'}
print(type(data))
json_data = json.dumps(data)
print(type(json_data))
print(json_data)
print(data)

