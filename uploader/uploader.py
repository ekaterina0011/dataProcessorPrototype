import requests
import json
import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()

if parser == 'food' :


class Uploader:

    def __init__(self, config):
        self.food_url=config.food_url
        self.food_min_batch_size = config.food_min_batch_size

    def get_data(self):
        response = requests.get(self.food_min_batch_size)
        return self.to_dataframe(json.loads(response.content))
    def to_dataframe(self, raw_data):
        spark = SparkSession \
            .builder \
            .appName("Python Spark SQL basic example") \
            .config("spark.jars", "./postgresql-42.5.3.jar") \
            .getOrCreate()
        return spark.createDataFrame(raw_data)
