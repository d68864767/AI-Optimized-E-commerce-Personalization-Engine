```python
# Import necessary libraries
from bigquery_handler import BigQueryHandler
from ai_platform_handler import AIPlatformHandler
from google.oauth2 import service_account

class InventoryOptimization:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.bigquery_handler = BigQueryHandler(credentials_path)
        self.ai_platform_handler = AIPlatformHandler(credentials_path)

    def get_inventory_data(self, dataset_id, table_id):
        """
        Get inventory data from BigQuery
        """
        return self.bigquery_handler.get_table_data(dataset_id, table_id)

    def predict_inventory_needs(self, model_id, input_data):
        """
        Predict inventory needs using AI Platform
        """
        return self.ai_platform_handler.predict(model_id, input_data)

    def update_inventory(self, dataset_id, table_id, rows_to_update):
        """
        Update inventory data in BigQuery
        """
        self.bigquery_handler.update_table(dataset_id, table_id, rows_to_update)

    def optimize_inventory(self, dataset_id, table_id, model_id):
        """
        Optimize inventory based on predictions
        """
        inventory_data = self.get_inventory_data(dataset_id, table_id)
        for index, row in inventory_data.iterrows():
            input_data = {
                'product_id': row['product_id'],
                'current_stock': row['current_stock'],
                'sales_rate': row['sales_rate']
            }
            prediction = self.predict_inventory_needs(model_id, input_data)
            if prediction[0] > row['current_stock']:
                rows_to_update = [{'product_id': row['product_id'], 'current_stock': prediction[0]}]
                self.update_inventory(dataset_id, table_id, rows_to_update)
```

