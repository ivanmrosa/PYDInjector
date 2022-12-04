from PyDInjector.test.data.interfaces.IFood import IFood, IFoodProvider
from abc import ABC

class ICooker(ABC):
    def __init__(self, foodProvider1 : IFoodProvider, foodProvider2 : IFoodProvider) -> None:
        pass

    def getFoods(self) -> list[IFood]:
        pass