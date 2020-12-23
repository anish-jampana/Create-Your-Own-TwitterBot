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

# txt file filled with my tweets (line by line, must be less than 280 char)
file = open("/Users/anishjampana/Downloads/tweets.txt", "r") # replace tweets.txt with sample.txt or your own txt file.

# reads line by line
filelines = file.readlines()

# closes once program reaches end of file
file.close()

# for loop to tweet each line by line every 24 hours (86400 seconds)
for line in filelines:
  print(line)
  if line != '\n':
      api.update_status(line)
  else:
      pass
  sleep(86400)
