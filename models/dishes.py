#Как указать нормально директорию?
import json
from config.cfg import Config
from uploader.uploader import UploaderObject
config = Config('C:/Users/Катя/PycharmProjects/dataProcessorPrototype/config/config.yml')
uploaderobj = UploaderObject(config) #тянем строку из мэина
str_json=uploaderobj.get_data() #обзываем ее str_json
data=json.loads(str_json) #получаем словарь (сделали в мэине)


class Dish: #Создаем класс, в котором делаем атрибуты-поля и
            # который кладем в эти поля всякое из словаря, которое достали из интернета
    def __init__(self):
        self.id = data['id']
        self.uid = data['uid']
        self.dish = data['dish']
        self.description = data['description']
        self.ingredient = data['ingredient']
        self.measurement = data['measurement']

c= Dish() #Обращаемся к классу, берем из него всякое
print(c.dish)




    #x=data["dish"] # доступ к элементам словаря
#print(x)
#print(type(data['uid']))
#print(data['uid'])
#for i in data.items(): # получаем пары словаря ("ключ", "знач")
    #print(type(i))
  #  print(i)
#for i in data:# получаем текстом ключи
    #print(type(i))
  #  print(i)
