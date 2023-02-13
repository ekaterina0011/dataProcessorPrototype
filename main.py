import pyspark
from config.cfg import Config
from uploader.uploader import Uploader


if __name__ == '__main__':
    config = Config('./config/config.yml')
    uploader=Uploader(config)
   # dish = class_schema(Dish).load(uploader.get_data())
    #pythonDict = json.loads(uploaderobj.get_data())
    #print(dish)
    #dishes.abc(uploaderobj.get_data()) #тут тип класса строка
    #pythonDict = json.loads(uploaderobj.get_data())
    print(type(uploader.get_data()))#тут тип класса- dick
    Dish_df= pyspark.
    #print(uploaderobj.get_data())  #тут тип класса строка
    #print(pythonDict)  #тут тип класса dict, можно использовать дальше в dishes
