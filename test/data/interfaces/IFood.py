from abc import ABC

class IFood(ABC):
    def getFoodName(self) -> str:
        pass    
    def getInstanceIdentification(self) -> str:
        pass

class IFoodProvider(ABC):
    def getFood(self) -> IFood:
        pass
    def getInstanceIdentification(self) -> str:
        pass
