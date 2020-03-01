import requests
url = "https://www.v2ex.com/api/topics/hot.json"
headers = {'cache-control' : "no-cache" }
response = requests.request("GET",url,headers=headers)

hot_topics = response.json()
assert len(hot_topics) > 9
print('Test case Passed')
