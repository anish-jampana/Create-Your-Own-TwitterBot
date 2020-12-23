import tweepy
from time import sleep

# variables for all the keys and tokens
consumer_key = "Fc0YhKevNcKK93UrnSWoF3KDv"
consumer_secret = "EWTx2j2B3swL1SbTOP8PyU84oYpwG3GmfFk5tSlgqnKNJbe1rg"
access_token = "1341182770056290304-c7R7TTZ6l22jJ2W2kuu4iZGVXDkCVG"
access_token_secret = "UB1xjeeAvGEwfTkSObtvFQUlCfHpVMdafOzdfSqZdOJSq"

# authentication from tweepy to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# txt file filled with my tweets (line by line, must be less than 280 char)
file = open("/Users/anishjampana/Downloads/tweets.txt", "r")

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
