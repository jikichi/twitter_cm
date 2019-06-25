# -*- coding: <encoding name> -*-
import tweepy
import os
import pandas
import json
import requests
from requests_oauthlib import OAuth1Session

from config import *
from open_fav_list import *
from get_retweeter_Id import *
from mk_matched_list import *
from lottery_wheel import *
from send_dm_message import *
from get_follower_ids_list import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

if __name__ == "__main__":
    followerIdsList = getFollowerIdsList(search_id, api, tweepy)
    retweeter_list = getretweeterId(tweetID, twitter, json) 
    fav_user_list = open_fav_list()
    print("retweeter")
    print(retweeter_list)
    print("*" * 20)
    print("fav")
    print(fav_user_list)
    print("*" * 20)
    print("follower")
    print(followerIdsList)
    print("*" * 20)   

    matched_list = mk_matched_list(followerIdsList, retweeter_list, fav_user_list)
    print(matched_list)
    send_message(lottery_wheel(matched_list), twitter, json)