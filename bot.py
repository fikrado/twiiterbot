import tweepy
import time

consumer_key = 'hU4anbsA7eNHHgkhKqIH3uApk'
consumer_secret = 'wH0Y1lcjieVHvp9ZWdc02peZXPoqd4y6t6cRo3rVJm9u6ypSSK'

key = '1279649205754171392-a86nTVpdAOxiW5yIW6aEkgkrqi0D4Z'
secret = 'CYHS7FEEwPLDCYZOctqyynMPwLxONbWdK396n0ljXQtxS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

search = 'somali'
search2 = 'hacking'
search3 = 'viral'
search4 = 'somaliland'
search5 = 'love'
search6 = 'cats'
search7 = 'code'

nrTweets = 50


for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search4).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search2).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search3).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search5).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search6).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search7).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
