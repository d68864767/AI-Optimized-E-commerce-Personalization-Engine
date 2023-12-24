```python
# Import necessary libraries
from bigquery_handler import BigQueryHandler
from natural_language_api_handler import NaturalLanguageAPIHandler

class MarketTrendAnalysis:
    def __init__(self, credentials_path):
        self.bigquery_handler = BigQueryHandler(credentials_path)
        self.natural_language_api_handler = NaturalLanguageAPIHandler()

    def get_market_data(self, dataset_id, table_id):
        """
        Get market data from BigQuery
        """
        return self.bigquery_handler.get_table_data(dataset_id, table_id)

    def analyze_market_sentiment(self, market_data):
        """
        Analyze the sentiment of market data using Google Cloud Natural Language API
        """
        sentiment_scores = []
        for data in market_data:
            sentiment_score, _ = self.natural_language_api_handler.analyze_sentiment(data)
            sentiment_scores.append(sentiment_score)

        return sentiment_scores

    def analyze_market_entities(self, market_data):
        """
        Analyze the entities of market data using Google Cloud Natural Language API
        """
        entity_analysis = []
        for data in market_data:
            entities = self.natural_language_api_handler.analyze_entities(data)
            entity_analysis.append(entities)

        return entity_analysis

    def analyze_market_trends(self, dataset_id, table_id):
        """
        Analyze market trends based on sentiment and entity analysis
        """
        market_data = self.get_market_data(dataset_id, table_id)
        sentiment_scores = self.analyze_market_sentiment(market_data)
        entity_analysis = self.analyze_market_entities(market_data)

        return sentiment_scores, entity_analysis
```

