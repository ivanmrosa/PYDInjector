from abc import ABC
from PyDInjector.test.data.interfaces.IFood import IFoodProvider

class IBody(ABC):
    def move(self) -> str:
        pass
    def jump(self) -> str:
        pass
    def getHandsQuantity(self) -> int:
        pass
    def getLegsQuantity(self) -> int:
        pass
    def getInstanceIdentification(self) -> str:
        pass    
    def getActionIdentification(self) -> str:
        pass    
    def eat(self, foodProvider: IFoodProvider) -> str:
        pass
