from PyDInjector.test.data.interfaces.IBodyAction import IBodyAction
import uuid

from PyDInjector.test.data.interfaces.IFood import IFood


class HumanBodyAction(IBodyAction):    
    def __init__(self) -> None:        
        super().__init__()
        self.__identification : str = str(uuid.uuid1())    
    def move(self) -> str:
        return 'moved'
    def jump(self) -> str:
        return 'jumped'
    def eat(self, food: IFood) -> str:
        return food.getFoodName()
    def getInstanceIdentification(self) -> str:
        return self.__identification