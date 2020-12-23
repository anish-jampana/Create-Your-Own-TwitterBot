# follows every account that is currently following you
for follower in tweepy.Cursor(api.followers).items():
    print("Following everyone that follows you!")
    follower.follow()
