# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #100DaysOfDoingSomething, limit to 100
for tweet in tweepy.Cursor(api.search,q='#100DaysOfDoingSomething').items(100):

    # Print out usernames of the last 100 people to use #100DaysOfDoingSomething
    try:
        print('Tweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Reply to the tweet
        api.update_status('Keep going @' + tweet.user.screen_name + ', it\'s worth it!', tweet.id)

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break