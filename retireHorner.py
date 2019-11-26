import requests
import json
url1 = "https://games.mobileapi.hupu.com/1/7.3.0/soccer/v2/player/honor?player_id="
n = 0
with open('retire.txt','r') as f:
    for playerId in f.readlines():
        urlNew= url1 + playerId.strip()
        data1 = requests.request("GET",urlNew)
        data2 = json.loads(data1.content)
        # code = data1.status_code
        # print(urlNew)
        # print(data2)
        if  len(data2["result"]["honor"]) > 0 :
            pass
            # for value in data2["result"]["honor"]:
            #    print(value,end=",")
            # print()
        else:
            print("球员荣誉是空:player_id="+playerId)
