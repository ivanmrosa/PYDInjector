from PyDInjector.test.data.interfaces.IFood import IFood
import uuid

class Pasta(IFood):
    def __init__(self) -> None:
        super().__init__()
        self.__id = str(uuid.uuid1())
    
    def getFoodName(self) -> str:
        return 'Pasta'
    
    def getInstanceIdentification(self) -> str:
        return self.__id

class Meat(IFood):
    def __init__(self) -> None:
        super().__init__()
        self.__id = str(uuid.uuid1())
    
    def getFoodName(self) -> str:
        return 'Meat'
    
    def getInstanceIdentification(self) -> str:
        return self.__id

class Rice(IFood):
    def __init__(self) -> None:
        super().__init__()
        self.__id = str(uuid.uuid1())
    
    def getFoodName(self) -> str:
        return 'Rice'
    
    def getInstanceIdentification(self) -> str:
        return self.__id
    