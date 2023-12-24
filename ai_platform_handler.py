```python
# Import necessary libraries
from google.cloud import aiplatform
from google.oauth2 import service_account

class AIPlatformHandler:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = aiplatform.gapic.PredictionServiceClient(credentials=self.credentials)

    def predict(self, model_id, input_data):
        """
        Make a prediction using a deployed model
        """
        endpoint = self.client.endpoint_path(project=self.credentials.project_id, location='us-central1', endpoint=model_id)
        response = self.client.predict(endpoint=endpoint, instances=[input_data])
        return response.predictions

    def train_model(self, dataset_id, model_display_name, target_column):
        """
        Train a new model
        """
        dataset = self.client.dataset_path(project=self.credentials.project_id, location='us-central1', dataset=dataset_id)
        model = {
            "display_name": model_display_name,
            "dataset_id": dataset_id,
            "target_column": target_column
        }
        response = self.client.create_model(parent=dataset, model=model)
        print("Training operation name: {}".format(response.operation.name))
        print("Training started...")

    def deploy_model(self, model_id, endpoint_display_name):
        """
        Deploy a trained model
        """
        endpoint = {
            "display_name": endpoint_display_name
        }
        response = self.client.create_endpoint(parent=self.credentials.project_id, endpoint=endpoint)
        endpoint = response.result()

        deployed_model = {
            "model": model_id,
            "automatic_resources": {
                "min_replica_count": 1,
                "max_replica_count": 1
            }
        }
        response = self.client.deploy_model(endpoint=endpoint.name, deployed_model=deployed_model)
        print("Deploy operation name: {}".format(response.operation.name))
        print("Deploying model to endpoint...")

    def undeploy_model(self, model_id):
        """
        Undeploy a model
        """
        response = self.client.undeploy_model(endpoint=model_id)
        print("Undeploy operation name: {}".format(response.operation.name))
        print("Undeploying model from endpoint...")
```

