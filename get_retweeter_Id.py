#リツートしたユーザーのIDを返します

def getretweeterId(tweetID, twitter, json):
    retweeterIdList = []
    url = "https://api.twitter.com/1.1/statuses/retweeters/ids.json?id="+tweetID+"&counnt=100&stringify_ids=true"
    retinfo = json.loads(twitter.get(url).text)
    for j in range(len(retinfo["ids"])):
        retweeterIdList.append(int(retinfo["ids"][j]))
    return(retweeterIdList)