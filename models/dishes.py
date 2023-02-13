from marshmallow_dataclass import dataclass

@dataclass
class Dish():
   id:str
   uid:str
   dish:str
   description:str
   ingredient:str
   measurement:str