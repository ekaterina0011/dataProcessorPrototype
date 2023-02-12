from config.cfg import Config
from uploader.uploader import Uploader
#from uploader.uploader import UploaderObject
#import json
if __name__ == '__main__':
    config = Config('./config/config.yml')
    uploader=Uploader(config)
    uploaderobj = UploaderObject(config)
    print(uploader.get_data())# тут тип класса- байты
    #print(uploaderobj.get_data())  #тут тип класса строка
    #pythonDict = json.loads(uploaderobj.get_data())
    #print(pythonDict)  #тут тип класса dict, можно использовать дальше в dishes