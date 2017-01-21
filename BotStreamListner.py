import tweepy, time, sys
class BotStreamListner(tweepy.StreamListener):
	def on_status(self,status):
		print(status.text)
	def on_error(Self,status_code):
		if status_code ==420:
			return False
	def on_data(self, data):
		print(data)
		decoded = json.loads(data)
		# listen only for tweets that is geo-location enabled
		print('heyy')
		try: 
			tweet = {}
			tweet['screen_name'] = '@'+decoded['user']['screen_name']
			tweet['text'] = decoded['text'].encode('ascii', 'ignore')
			if decoded['coordinates']:
				tweet['coordinates'] = decoded['coordinates']['coordinates']
				tweet['created_at'] = decoded['created_at']
				print('A tweet received')
				print(tweet)
				# publish to 'tweet_stream' channel
				return True
			else:
				pass

		except:
			pass
