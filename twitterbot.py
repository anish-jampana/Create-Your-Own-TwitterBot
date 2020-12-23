import tweepy
from time import sleep

# variables for all the keys and tokens
consumer_key = "Add your own"
consumer_secret = "Add your own"
access_token = "Add your own"
access_token_secret = "Add your own"

# authentication from tweepy to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# add code from tweetfile.py here if you want to your robot to automatically tweet at certain time intervals
# add code from follow.py here if you want to follow every account that follows you
