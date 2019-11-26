import requests
import json

#http GET接口返回值为json的通用方法
def httpGetJson(url,querystring):
    #print(querystring)
    response = requests.request("GET", url, params=querystring)
    #print(response.url)
    code=response.status_code
    text=response.text
    #print(text)
    return code,json.loads(text)

# #http GET接口返回值为json的通用方法
# def httpGetJsonResponseTime(url,querystring):
#     response = requests.request("GET", url, params=querystring)
#     code=response.status_code
#     responseTime=response.elapsed.total_seconds()
#     return code,json.loads(response.text),responseTime




if __name__ == '__main__':
    # querystring={"team_id":"357",
    #              "players":"45334",
    #              "types":"7,8,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54",
    #              "season_id":"2018",
    #              "league_id":"357"}
    # querystring ={'team_id': '150',
    #               'players': '32095',
    #               'season_id': '2019',
    #               'types': '7,8,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54',
    #               'league_id': '150'}
    # url = "http://gdc-test.hupu.com/api/soccer/scrank/seasonPlayerCount"
    url="https://gdc-soccerapi-tst.hupu.com/soccer/player-data/v2/5467979"
    querystring={}
    code,getJson=httpGetJson(url,querystring)
    print(code,getJson)
