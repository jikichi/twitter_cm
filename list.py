import requests
from ../config import *
def get_fav_users(tweet_id):
    url = 'https://twitter.com/i/activity/favorited_popup?id='
    url = url + str(tweet_id)
    data = requests.get(url)
    data = str(data.json())

    with open('tweet.html', 'w') as f:
        f.write(data)

    data = data.split('data-user-id')

    user_list = []

    for i in data:
        infos = i.split()
        for info in infos:
            if info[0] == '=' and info[1] == '"' and info[-1] == '"':
                user_list.append(info.replace('"', '').replace('=', ''))
    
    return list(map(int, set(user_list)))


def add_fav_list(tweetID):
    even_list = []
    new_list =[]
    try:
        with open('../fav_list.txt') as f2:
            a = f2.read()
            if (a):
                even_list = a.split(",")
            even_list = filter(lambda a: a != "", even_list)
            new_list = [int(float(x)) for x in even_list]
    except:
        print("don't have list.txt, so make it")

    with open('fav_list.txt', 'w') as f: 
        
        get_fav_list = get_fav_users(tweetID)

        for x in get_fav_list:
            new_list.append(x)

        #new_list = map(int, set(new_list))
        print(new_list)
        for x in new_list:
            f.write(str(x) + ",")

add_fav_list(tweetID)
