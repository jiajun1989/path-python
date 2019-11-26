import requests
import json
url = "https://test.mobileapi.hupu.com/3/7.3.23/fifa/getMatchs?client=0A788E40-FA31-470B-8040-8D393497C254&limit=500"
data1 = requests.request("GET",url)
data2 = json.loads(data1.content)
data3 = data2["result"]["games"]
# print(data2["result"]["games"])
for match in data3:
    print(match["data"])
    # if data3[i]






