import uuid
from PyDInjector.PyDInjector import inject
from PyDInjector.test.data.interfaces.IBody import IBody
from PyDInjector.test.data.interfaces.IBodyAction import IBodyAction
from PyDInjector.test.data.interfaces.IFood import IFoodProvider

class HumanBody(IBody):    

    @inject
    def __init__(self, actions: IBodyAction) -> None:        
        super().__init__()
        self.__actions : IBodyAction = actions
        self.__identification : str = str(uuid.uuid1())    
    def move(self) -> str:
        return self.__actions.move()
    def jump(self) -> str:
        return self.__actions.jump()
    def getLegsQuantity(self) -> int:
        return 2
    def getHandsQuantity(self) -> int:
        return 2
    def getInstanceIdentification(self) -> str:
        return self.__identification
    def getActionIdentification(self) -> str:
        return self.__actions.getInstanceIdentification()
    @inject
    def eat(self, foodProvider: IFoodProvider) -> str:
        return self.__actions.eat(food=foodProvider.getFood())
    