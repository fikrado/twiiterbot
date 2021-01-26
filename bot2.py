# this is a profissional tweeter bot make sure you have 
# api from tweeter developer accont then you are ready
# tweet thanks @mr__yahye is my tweeter id  

import tweepy
import time
from keep_alive import keep_alive
import os
import random
import json
from pathlib import Path
import csv
#the web server
keep_alive()

#but your api keys here

consumer_key = 'hU4anbsA7eNHHgkhKqIH3uApk'
consumer_secret = 'wH0Y1lcjieVHvp9ZWdc02peZXPoqd4y6t6cRo3rVJm9u6ypSSK'

key = '1279649205754171392-a86nTVpdAOxiW5yIW6aEkgkrqi0D4Z'
secret = 'CYHS7FEEwPLDCYZOctqyynMPwLxONbWdK396n0ljXQtxS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#but your own keywords here

search = '@africa'
search2 = 'moltivation'
search3 = '@somali'
search4 = 'tryhackme'
search5 = '@liveoverflow'
search6 = 'bot'
search7 = '@mfarmajo'
search8 = 'machenlearning'
search9 = 'musebixi'
search10 = 'blacklivematter'
search11 = 'netcat'
search12 = 'python'
search13 = 'unitednations'
search14 = 'hashcat'
search15 = 'johntherepper'
search16 = 'nmap'

nrTweets = 176

#make any coment in save stus pro tip use pycharm to make change in click

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search4).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search2).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search3).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search5).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search6).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search7).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search8).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search9).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search10).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search11).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search12).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search13).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search14).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search15).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search16).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        api.update_status(status='i always tweet a real inspiring and moltivation tweet make sure you flow i love you')
        time.sleep(84000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



ROOT = Path(__file__).resolve().parents[0]


def get_tweet(tweets_file, excluded_tweets=None):
    """Get tweet to post from CSV file"""

    with open(tweets_file) as csvfile:
        reader = csv.DictReader(csvfile)
        possible_tweets = [row["tweet"] for row in reader]

    if excluded_tweets:
        recent_tweets = [status_object.text for status_object in excluded_tweets]
        possible_tweets = [tweet for tweet in possible_tweets if tweet not in recent_tweets]

    selected_tweet = random.choice(possible_tweets)

    return selected_tweet


def lambda_handler(event, context):
    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Get tweet from csv file")
    tweets_file = ROOT / "tweets.csv"
    recent_tweets = api.user_timeline()[:3]
    tweet = get_tweet(tweets_file)

    print(f"Post tweet: {tweet}")
    api.update_status(tweet)

    return {"statusCode": 200, "tweet": tweet}
