import os
import sys
import argparse
from service.aggr_funcs import Aggr_Data
from database.dbloader import Provider
from config.cfg import Config
from uploader.uploader import Uploader
from datetime import datetime
from pyspark.sql import SparkSession


if __name__ == '__main__' :
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    parser = argparse.ArgumentParser()
    parser.add_argument("-ds", help= 'data source: food or dessert' )
    parser.add_argument("-dt", help= 'date(optional)')
    # TO-DO handle error
    args = parser.parse_args()

    config = Config('./config/config.yml', args.ds, args.dt)
    spark_session = SparkSession \
        .builder \
        .appName(config.spark_app_name) \
        .config(config.spark_config_key, config.spark_config_value) \
        .getOrCreate()

    uploader = Uploader(config)

    raw_data = uploader.get_data()
    dataframe = uploader.to_dataframe(spark_session, raw_data)
    db_provider = Provider(config)
    db_provider.insert(spark_session, dataframe)


    df = spark_session.read.format("jdbc") \
    .option('dbtable', config.request_history_table) \
    .option("url", config.db_url) \
    .option("driver", "org.postgresql.Driver")\
    .option("user", "postgres")\
    .option("password", "postgres").load()
    data_source=config.data_source
    load_dttm=config.date
    asd = Aggr_Data(spark_session,df,data_source,load_dttm)

