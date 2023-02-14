import uploader.dbloader as upl
from config.cfg import Config
from uploader.uploader import Uploader
from pyspark.sql import SparkSession
import os
import sys

if __name__ == '__main__':

    config = Config('./config/config.yml')
    uploader = Uploader(config)
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.jars", "./postgresql-42.5.3.jar") \
        .getOrCreate()

    dataDict = uploader.get_data()
    #a = fib(dataDict)
    dbl=upl.abc(dataDict,spark)
    dbl.show()

    mode = "append"
    url = "jdbc:postgresql://localhost:5432/postgres"
    properties = {"user": "postgres", "password": "postgres", "driver": "org.postgresql.Driver"}
    dbl.write.jdbc(url=url, table="task1.food", mode=mode, properties=properties)

    print(dbl)
    # a= fib(17) #как передавать параметры
    # dish = class_schema(Dish).load(uploader.get_data())
    # pythonDict = json.loads(uploaderobj.get_data())
    # print(dish)
    # dishes.abc(uploaderobj.get_data()) #тут тип класса строка
    # pythonDict = json.loads(uploaderobj.get_data())
    # print(type(uploader.get_data()))#тут тип класса- dickt
    # Dish_df= pyspark.
    # print(uploaderobj.get_data())  #тут тип класса строка
    # print(pythonDict)  #тут тип класса dict, можно использовать дальше в dishes
