```python
# Import necessary libraries
from google.cloud import bigquery
from google.oauth2 import service_account

class BigQueryHandler:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = bigquery.Client(credentials=self.credentials, project=self.credentials.project_id)

    def execute_query(self, query):
        """
        Execute a SQL query
        """
        query_job = self.client.query(query)
        return query_job.result()

    def get_table_data(self, dataset_id, table_id):
        """
        Get data from a specific table
        """
        table_ref = self.client.dataset(dataset_id).table(table_id)
        table = self.client.get_table(table_ref)
        return self.client.list_rows(table).to_dataframe()

    def insert_rows(self, dataset_id, table_id, rows_to_insert):
        """
        Insert new rows into a table
        """
        table_ref = self.client.dataset(dataset_id).table(table_id)
        table = self.client.get_table(table_ref)
        errors = self.client.insert_rows(table, rows_to_insert)
        if errors:
            print('Encountered errors while inserting rows: {}'.format(errors))
        else:
            print('Rows inserted successfully.')

    def update_table(self, dataset_id, table_id, rows_to_update):
        """
        Update existing rows in a table
        """
        table_ref = self.client.dataset(dataset_id).table(table_id)
        table = self.client.get_table(table_ref)
        errors = self.client.update_rows(table, rows_to_update)
        if errors:
            print('Encountered errors while updating rows: {}'.format(errors))
        else:
            print('Rows updated successfully.')
```

