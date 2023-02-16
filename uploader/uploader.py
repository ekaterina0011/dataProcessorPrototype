import requests
import json

class Uploader:
    def __init__(self, config):
        self.api_url = config.api_url
        self.batch_size = config.batch_size
        self.spark_app_name = config.spark_app_name
        self.spark_config_key = config.spark_config_key
        self.spark_config_value = config.spark_config_value

    def get_data(self):
        response = requests.get(self.api_url+'?size='+str(self.batch_size))
        return json.loads(response.content)

    def to_dataframe(self, spark_session, raw_data):
        df = spark_session.createDataFrame(raw_data)
        df.drop(df.id)
        return df
