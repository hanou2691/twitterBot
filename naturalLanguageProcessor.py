# Imports the Google Cloud client library
from google.cloud import language

class naturalLanguageProcessor():
    keyword = ''
    entities = []

    def __init__(self, text):
        language_client = language.Client()        
        # Instantiates a client
        language_client = language.Client()

        # The text to analyze
        text = 'Hello, world! Starbucks coffee canada'
        #document = language_client.document_from_text(text)

        document = language_client.document_from_text(text)
        entities = document.analyze_entities()
    
        for entity in entities:
            if entity.entity_type == "CONSUMER_GOOD":     
                self.keyword = entity.name
                return
            elif entity.entity_type == "ORGANIZATION":    
                self.keyword = entity.name
                return
            elif entity.entity_type == "LOCATION":
                self.keyword = entity.name
                return               
                

            print('=' * 20)
            print('{:<16}: {}'.format('name', entity.name))
            print('{:<16}: {}'.format('type', entity.entity_type))
            print('{:<16}: {}'.format('wikipedia_url', entity.wikipedia_url))
            print('{:<16}: {}'.format('metadata', entity.metadata))
            print('{:<16}: {}'.format('salience', entity.salience))

    def has_keyword(self):
        return self.keyword != ''
    
    def get_keyword(self):
        return self.keyword