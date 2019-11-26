import requests
import json
url1 = "https://gdc-soccerapi.hupu.com/soccer/player-data/v2/"

with open('retire.txt','r') as f:
    for playerId in f.readlines():
        urlNew= url1 + playerId.strip()
        data1 = requests.request("GET",urlNew)
        data2 = json.loads(data1.content)
        code = data1.status_code
        # print(urlNew)
        # print(data2)
        if code ==200 and data2["data"] :
            for key,value in data2["data"].items():
               print(value,end=",")
            print()
        else:
            print("这是坏的:"+playerId)
