```python
# Import necessary libraries
from google.cloud import appengine
from google.oauth2 import service_account
from flask import Flask, render_template, request

class AppEngineHandler:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = appengine.ApplicationsClient(credentials=self.credentials)
        self.app = Flask(__name__)

    def create_app(self):
        """
        Create a new App Engine application
        """
        app = self.client.create_application(
            parent=self.credentials.project_id,
            application={
                'id': self.credentials.project_id,
                'location_id': 'us-central',
                'serving_status': appengine.ServingStatus.SERVING,
            },
        )
        print(f'Created App Engine application {app.name}')

    def deploy_app(self):
        """
        Deploy the App Engine application
        """
        version = self.client.deploy_version(
            parent=f'projects/{self.credentials.project_id}/services/default',
            version={
                'runtime': 'python39',
                'entrypoint': {
                    'shell': 'gunicorn -b :$PORT main:app',
                },
                'deployment': {
                    'cloud_build_options': {
                        'app_yaml_path': 'app.yaml',
                    },
                },
                'automatic_scaling': {
                    'target_cpu_utilization': 0.65,
                    'min_instances': 1,
                },
            },
        )
        print(f'Deployed version {version.id} of the App Engine application')

    def run_app(self):
        """
        Run the App Engine application
        """
        @self.app.route('/')
        def home():
            return render_template('index.html')

        @self.app.route('/dashboard')
        def dashboard():
            return render_template('dashboard.html')

        if __name__ == '__main__':
            self.app.run(host='127.0.0.1', port=8080, debug=True)
```
