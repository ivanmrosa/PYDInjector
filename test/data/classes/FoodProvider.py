import uuid
from PyDInjector.test.data.interfaces.IFood import IFood, IFoodProvider
from PyDInjector.test.data.classes.Food import Meat, Pasta, Rice

class FoodProvider(IFoodProvider):
    def __init__(self) -> None:
        super().__init__()
        self.__index = -1
        self.__foods = [Meat(), Pasta(), Rice()]
        self.__id = str(uuid.uuid1())
            
    def getFood(self) -> IFood:
        self.__index += 1    
        if self.__index >= len(self.__foods):
            self.__index = -1
        
        return self.__foods[self.__index]

    def getInstanceIdentification(self) -> str:
        return self.__id
