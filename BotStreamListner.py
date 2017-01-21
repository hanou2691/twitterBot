import tweepy, time, sys
class BotStreamListner(tweepy.StreamListener):
	def on_status(self,status):
		print(status.text)
	def on_error(Self,status_code):
		if status_code ==420:
			return False
