import mysqlTest
import httpGetJson
import time
#从数据库取playid
host="gdc-soccerleida-01.offline.hupu.com"
username="root"
password="gdc"
database="gdc_soccer_core"
port=3306

querySql="SELECT * from gdc_soccer_player where name_en is not NULL and op_id is NULL"
#querySql="SELECT * from gdc_soccer_player where name_en is not NULL and op_id is not NULL"
mysql1=mysqlTest.mysqlClient(host, username,password, database,3306)
players=mysql1.queryAll(querySql)
#players=mysql1.queryMany(querySql,50)
mysql1.mysqlClose()
playerIdList=[]
for player in players:
    playerIdList.append(player[1])

print(len(playerIdList))
#print(len(playerIdList),playerIdList)

#playerIdList=[50000002, 50000003, 50000004, 50000005, 12970740, 50000006, 15872198, 12970620, 14277868, 50000007]

# with open("存在名字且存在opid的球员.csv","w") as f:
#     #存在名字且存在opid的，对比新老接口
#     # 1:是否都有数据返回
#     f.write("playerId,oldApi,newApi\n")
#     for playerId in playerIdList:
#         oldApiUrl="https://test.mobileapi.hupu.com/3/7.3.27/soccer/v2/player/m_info"
#         oldquerystring={"player_id" : playerId}
#         newApiUrl="https://gdc-soccerapi-tst.hupu.com/soccer/player-data/v2/"+str(playerId)
#         # print(newApiUrl)
#         newquerystring={}
#         oldcode,oldJson=httpGetJson.httpGetJson(oldApiUrl,oldquerystring)
#         newcode,newJson=httpGetJson.httpGetJson(newApiUrl,newquerystring)
#         if oldcode==200 and newcode==200:
#             # print(oldJson)
#             # print(newJson)
#             if "result" in oldJson.keys():
#                 if "player_info" in oldJson["result"]:
#                     if newJson["code"]==200 and len(oldJson["result"]["player_info"])>0:
#                         pass
#                     else:
#                         f.write(str(playerId)+","+str(len(oldJson["result"]["player_info"]))+","+str(newJson["code"])+"\n")
#                 else:
#                     f.write(str(playerId) + ",error," + str(
#                                 newJson["code"])+"\n")
#             else:
#                 f.write(str(playerId) + ",error," + str(
#                     newJson["code"])+"\n")
#         #time.sleep(1)
            # print(oldJson["result"]["play_info"])
            # print(newJson["data"])


with open("存在名字但不存在opid的球员.csv","w") as w:
    w.write("playerId,newApiCode\n")
    #存在名字但不存在opid的确定新接口可以正常返回
    n=0
    for playerId in playerIdList:
        print(n)
        newApiUrl="https://gdc-soccerapi-tst.hupu.com/soccer/player-data/v2/"+str(playerId)
        newquerystring={}
        newcode,newJson=httpGetJson.httpGetJson(newApiUrl,newquerystring)
        if newcode==200:
            if newJson["code"]!=200:
                w.write(str(playerId)+","+str(newJson["code"])+"\n")
                w.flush()
        n=n+1
    #time.sleep(1)
        # print(oldJson["result"]["play_info"])
        # print(newJson["data"])