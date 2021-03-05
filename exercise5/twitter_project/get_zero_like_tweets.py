import requests
import json



BEARER_TOKEN = ""


tweets = []
with open("tweets.txt") as infile:
    for line in infile:
        tweets.append(json.loads(line.strip()))

tweet_ids = [tweet["data"]["id"] for tweet in tweets]

headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

tweets_with_metrics = []

for i in range(0,len(tweet_ids),100):
    r = requests.get("https://api.twitter.com/2/tweets?ids={}&tweet.fields=public_metrics".format(",".join(tweet_ids[i:i+100])), headers=headers)
    tweets_with_metrics += json.loads(r.text)["data"]

zero_like_tweets = [x for x in tweets_with_metrics if x["public_metrics"]["like_count"] == 0]

with open("./zero_like_tweets.json","w") as outfile:
    json.dump(zero_like_tweets,outfile,ensure_ascii=False)
