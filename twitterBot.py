from tweepy import OAuthHandler
from tweepy import Stream
from google.cloud import language
from credentials import *
from botStreamListner import *
 
# Access and authorize Twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

language_client = language.Client()

streamListener = botStreamListner(api, language_client)
stream = tweepy.Stream(auth= api.auth,listener = streamListener)

try: 
    stream.filter(track=['#askYP'],async=True)
except:
    print("error")
    stream.disconnect()