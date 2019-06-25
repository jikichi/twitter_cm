
def getFollowerIdsList(search_id, api, tweepy):
    
    followers_ids = tweepy.Cursor(api.followers_ids, id = search_id, cursor = -1).items()
    followers_ids_list = []

    try:
        for followers_id in followers_ids:
            followers_ids_list.append(followers_id)

    except tweepy.error.TweepError as e:
        print (e.reason)

    return followers_ids_list