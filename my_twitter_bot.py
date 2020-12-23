import tweepy
from time import sleep
print('this is my twitter bot')

consumer_key = "Add your own"
consumer_secret = "Add your own"
access_token = "Add your own"
access_token_secret = "Add your own"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

file = open("/Users/anishjampana/Downloads/tweets.txt", "r")
filelines = file.readlines()
file.close()

for line in filelines:
  print(line)
  if line != '\n':
      api.update_status(line)
  else:
      pass
  sleep(86400)
