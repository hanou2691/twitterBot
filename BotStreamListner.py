import tweepy
import json

class botStreamListner(tweepy.StreamListener):
	def on_status(self,status):
		print(status.text)
	def on_error(Self,status_code):
		print(status_code)
		if status_code ==420:
			return False
	def on_data(self, data):
		print(data)
		decoded = json.loads(data)		
		try: 
			tweet = {}
			tweet['screen_name'] = '@'+decoded['user']['screen_name']
			tweet['text'] = decoded['text'].encode('ascii', 'ignore')
			print('A tweet received')
			if decoded['place']['bounding_box']['coordinates']:
				print("Has coordinates")
				tweet['coordinates'] = decoded['place']['bounding_box']['coordinates']
				tweet['created_at'] = decoded['created_at']				
				# publish to 'tweet_stream' channel
				return True
			else:
				print("Doesn't have coordinates")
				pass
			print(tweet['text'])		
		except:
			pass
