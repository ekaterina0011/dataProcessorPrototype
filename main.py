from config.cfg import Config
from uploader.uploader import Uploader

import os
import sys

if __name__ == '__main__':

    config = Config('./config/config.yml')
    uploader = Uploader(config)

    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    dataframe = uploader.get_data()
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
