import requests
import json

class Uploader:
    def __init__(self, config):
        self.url=config.url
        self.batch_size = config.batch_size

    def get_data(self):
        response = requests.get(self.url)
        return json.loads(response.content)