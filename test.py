import json
from config import *
from requests_oauthlib import OAuth1Session
from get_retweeter_Id import *
import json

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
tweetID = "1121215938362130432"
a_list = getretweeterId(tweetID, twitter, json)
print(a_list)