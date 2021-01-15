import tweepy
import time


consumer_key = 'hU4anbsA7eNHHgkhKqIH3uApk'
consumer_secret = 'wH0Y1lcjieVHvp9ZWdc02peZXPoqd4y6t6cRo3rVJm9u6ypSSK'

key = '1279649205754171392-a86nTVpdAOxiW5yIW6aEkgkrqi0D4Z'
secret = 'CYHS7FEEwPLDCYZOctqyynMPwLxONbWdK396n0ljXQtxS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

search = 'python, somali, ethicalhacker, cyberscurity, CCNA, CCNP, somaliland, pentester, tech, it, un, unitednations '
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        tweet.favorite()
        tweet.retweet()
        time.sleep(11000)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
