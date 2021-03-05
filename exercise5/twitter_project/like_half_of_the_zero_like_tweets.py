import requests
from requests_oauthlib import OAuth1
import json


API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""




with open("zero_like_tweets.json") as infile:
    tweets = json.load(infile)
tweet_ids = [x["id"] for x in tweets]

auth = OAuth1(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

i = 0
with open("liked_tweet_ids.txt","a") as liked_out:
    with open("nonliked_tweet_ids.txt","a") as nonliked_out:
        for tweet_id in tweet_ids:
            if i%2==0:
                liked_out.write(tweet_id + "\n")
                r = requests.post("https://api.twitter.com/1.1/favorites/create.json?id={}".format(tweet_id),auth=auth)
                if r.status_code == 200:
                    print("Tweet with id {} was successfully liked.".format(tweet_id))
                    liked_out.write(tweet_id + "\n")
                else:
                    print("Encountered a problem when trying to like tweet with id {}:".format(tweet_id))
                    print("Status: {}".format(r.status_code))
                    print(r.text)
                liked_out.write(tweet_id + "\n")
            else:
                print("Tweet with id {} was not liked.".format(tweet_id))
                nonliked_out.write(tweet_id + "\n")
            i+=1
