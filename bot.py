# this code created by yahye and othr random developer i dont remeber his Name 
# tweet thanks in @mr__yahye it double __ remember  
# yeah its my oficail tweeter acount

import tweepy
import time

#but your api keys here

consumer_key = 'hU4anbsA7eNHHgkhKqIH3uApk'
consumer_secret = 'wH0Y1lcjieVHvp9ZWdc02peZXPoqd4y6t6cRo3rVJm9u6ypSSK'

key = '1279649205754171392-a86nTVpdAOxiW5yIW6aEkgkrqi0D4Z'
secret = 'CYHS7FEEwPLDCYZOctqyynMPwLxONbWdK396n0ljXQtxS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#but your own keywords here

search = 'somali'
search2 = 'hacking'
search3 = 'viral'
search4 = 'somaliland'
search5 = 'love'
search6 = 'java'
search7 = 'code'
search8 = 'usa'
search9 = 'canada'
search10 = 'kalilinux'
search11 = 'cybersecurity'
search12 = 'python'
search13 = 'brutalforce'
search14 = 'github'
search15 = 'linux'
search16 = 'cisco'

nrTweets = 50

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
#### the code is end bye 
