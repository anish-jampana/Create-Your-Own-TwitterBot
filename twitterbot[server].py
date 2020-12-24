import tweepy
from time import sleep

# variables for all the keys and tokens
consumer_key =
consumer_secret =
access_token =
access_token_secret =

# authentication from tweepy to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

a_file = open("/Users/anishjampana/Downloads/tweets.txt", "r") # use your own txt file or sample.txt from repo
first_line = a_file.readline()
api.update_status(status = (first_line))
lines = a_file.readlines()
a_file.close()



del lines[0]

new_file = open("/Users/anishjampana/Downloads/tweets.txt", "w+") # use your own txt file or sample.txt from repo

for line in lines:
    new_file.write(line)

new_file.close()
