import requests
import json
class Uploader:
    def __init__(self, config):
        self.url=config.url
        self.batch_size = config.batch_size

    def get_data(self):
        response = requests.get(self.url)
        return response.content

class UploaderObject:
    def __init__(self, config):
        self.url=config.url
        self.batch_size = config.batch_size

    def get_data(self):
        response = requests.get(self.url)
        return json.dumps(response.json())