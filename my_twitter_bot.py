import tweepy
from time import sleep
print('this is my twitter bot')

consumer_key = "Fc0YhKevNcKK93UrnSWoF3KDv"
consumer_secret = "EWTx2j2B3swL1SbTOP8PyU84oYpwG3GmfFk5tSlgqnKNJbe1rg"
access_token = "1341182770056290304-c7R7TTZ6l22jJ2W2kuu4iZGVXDkCVG"
access_token_secret = "UB1xjeeAvGEwfTkSObtvFQUlCfHpVMdafOzdfSqZdOJSq"

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
