import tweepy, time, sys
from credentials import *
from BotStreamListner import *
 
# Access and authorize Twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

botStream = BotStreamListner();
myStream = tweepy.Stream(auth= api.auth,listener = botStream)
myStream.filter(track=['#askPY'],async=True)