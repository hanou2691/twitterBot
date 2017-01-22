# Imports the Google Cloud client library
from google.cloud import language

# Instantiates a client
language_client = language.Client()

# The text to analyze
text = 'Hello, world! Starbucks coffee canada'
#document = language_client.document_from_text(text)

document = language_client.document_from_text(text)
entities = document.analyze_entities()

for entity in entities:
    if entity.entity_type == "CONSUMER_GOOD":    
        pass
    elif entity.entity_type == "ORGANIZATION":
        pass
    elif entity.entity_type == "LOCATION":
        pass
    print('=' * 20)
    print('{:<16}: {}'.format('name', entity.name))
    print('{:<16}: {}'.format('type', entity.entity_type))
    print('{:<16}: {}'.format('wikipedia_url', entity.wikipedia_url))
    print('{:<16}: {}'.format('metadata', entity.metadata))
    print('{:<16}: {}'.format('salience', entity.salience))