```python
# Import necessary libraries
from google.cloud import language_v1
from google.cloud.language_v1 import enums

class NaturalLanguageAPIHandler:
    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of a text string using Google Cloud Natural Language API
        """
        document = language_v1.types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
        )
        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        return sentiment.score, sentiment.magnitude

    def analyze_entities(self, text):
        """
        Analyze the entities of a text string using Google Cloud Natural Language API
        """
        document = language_v1.types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
        )
        entities = self.client.analyze_entities(document=document).entities

        return entities

    def analyze_syntax(self, text):
        """
        Analyze the syntax of a text string using Google Cloud Natural Language API
        """
        document = language_v1.types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
        )
        syntax = self.client.analyze_syntax(document=document)

        return syntax
```
