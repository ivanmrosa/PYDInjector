from abc import ABC

from PyDInjector.test.data.interfaces.IFood import IFood

class IBodyAction(ABC):
    def move(self) -> str:
        pass
    def jump(self) -> str:
        pass
    def eat(self, food : IFood) -> str:
        pass
    def getInstanceIdentification(self) -> str:
        pass    



