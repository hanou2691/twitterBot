import tweepy
import json
import yellowPagesParser
import requests 

class botStreamListner(tweepy.StreamListener):
	def __init__(self, api, client):
		self.api = api
		self.language_client = client

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
			tweet['text'] = decoded['text']
			if decoded['place']['bounding_box']['coordinates']:
				tweet['coordinates'] = decoded['place']['bounding_box']['coordinates']	
				print(tweet['coordinates'])

				# Parse the text using Google Cloud API		
				try :
					document = self.language_client.document_from_text(str(tweet["text"]))
					entities = document.analyze_entities()
				except :
					print("error parsing")

				keyword = ''
				for entity in entities:
					if entity.entity_type == "CONSUMER_GOOD":    
						keyword = entity.name
					elif entity.entity_type == "ORGANIZATION":
						keyword = entity.name
					elif entity.entity_type == "LOCATION":
						keyword = entity.name
					print('=' * 20)
					print('{:<16}: {}'.format('name', entity.name))
					print('{:<16}: {}'.format('type', entity.entity_type))
					print('{:<16}: {}'.format('wikipedia_url', entity.wikipedia_url))
					print('{:<16}: {}'.format('metadata', entity.metadata))
					print('{:<16}: {}'.format('salience', entity.salience))
				
				# Query the YP API for a locationsa
				print(keyword)
				urlposition = "http://dcr.yp.ca/api/search/popular?keyword="+keyword
				myResponse = requests.get(urlposition)
				print(myResponse)
				url = ''
				if myResponse.ok:
					print('response ok')
					jData = json.loads(myResponse.content)
					for result in jData["data"]:
						print('in result')
						if result["result"]["Translation"]:
							print('in translation')
							if result["result"]["Translation"]["en"]["url"]:
								print("in url")
								url = result["result"]["Translation"]["en"]["url"]
								print(url)

				# Tweet the answer
				try :
					status = tweet['screen_name'] + " Here you go : " + url
					print(status)
					self.api.update_status(status = status)
				except :
					print("error responding to tweet")

				return True
			else:
				print("Doesn't have coordinates")
				pass
			print(tweet['text'])		
		except:
			pass
