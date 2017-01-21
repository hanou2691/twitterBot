from tweepy import OAuthHandler
from tweepy import Stream
from credentials import *
from BotStreamListner import *
 
# Access and authorize Twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

streamListener = botStreamListner()
stream = tweepy.Stream(auth= api.auth,listener = streamListener)

try: 
    stream.filter(track=['#askYP'],async=True)
except:
    print("error")
    stream.disconnect()