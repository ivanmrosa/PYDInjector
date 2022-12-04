from PyDInjector.PyDInjector import inject
from PyDInjector.test.data.interfaces.ICooker import ICooker
from PyDInjector.test.data.interfaces.IFood import IFood, IFoodProvider

class Cooker(ICooker):
    @inject
    def __init__(self, foodProvider1: IFoodProvider, foodProvider2: IFoodProvider) -> None:
        self.__foodProvider1 = foodProvider1
        self.__foodProvider2 = foodProvider2
    
    def getFoods(self) -> list[IFood]:
        return [self.__foodProvider1.getFood(), self.__foodProvider2.getFood()]