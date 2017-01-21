import tweepy, time, sys
from credentials import *
from BotStreamListner import *
 
# Access and authorize Twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# Redirect user to Twitter to authorize
redirect_user(auth.get_authorization_url())

# Get access token
auth.get_access_token("verifier_value")

# Construct the API instance
api = tweepy.API(auth)

botStream = BotStreamListner()
myStream = tweepy.Stream(auth= api.auth,listener = botStream)
myStream.filter(track=['#askPY'],async=True)
