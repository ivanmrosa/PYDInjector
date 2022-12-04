# PYDInjector
**Simple Dependency Injection Container for python**

## Description

PyDInjector is dependency injector container that facilitates to follow the *Inversion of Control* principle. PyDInjector uses the python type hint to
resolve the dependencies and to inject them into the objects. To do that we need to configurate the relation of the implementated objects with their types
(Interfaces/ABC). After configurated is possible to use the *@inject* decorator to indicates whether the container should inject the dependency.

There are to types of injections: the scoped injection and the singleton injection.

### Scoped injection

Escoped injection will provide a new instance of the object always that the scope where the @inject decorator was used is call. For example, if we decorate
the constructor *def __ini__(OurService : IOurService):*, the container will provide a new instance of *OurService* always whe instanciate this object. But 
if we decorate other method in this class like *def doSomenthing(OurService : IOurService):*, the container will provide a new instance of *OurService* 
always that we execute the method *doSomenthing*.

### Singleton injection

Singleton injection will instantiate the object once and then provide the same instance every time it been requested.

##Configuring the container injector

The configuration of the relationship between the types and the objects must be inserted at the begining of the code execution. In order to be able to 
do that is necessary to import the  *DIContainer* from *PyDInjector*. Then is possible to use the methods 
*DIContainer.AddScoped* and *DIContainer.AddSingleton*.


    from PyDInjector import DIContainer
    DIContainer.AddScoped(IBody, HumanBody)
    DIContainer.AddScoped(IBodyAction, HumanBodyAction)
    DIContainer.AddScoped(IFoodProvider, FoodProvider)
    DIContainer.AddSingleton(ICooker, Cooker)

The first parameter is the Interface and the second one is the class implementation.

See the utilization below:


    
    class HumanBody(IBody):    
        @inject #The container will inject a instance of BodyAction to this constursctor
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
        @inject #The container will inject a instance of FoodProvider tho this method. If the configuration was singleton, then will be always the same instance. Otherwise a new instance will be provided at each execution 
        def eat(self, foodProvider: IFoodProvider) -> str:
            return self.__actions.eat(food=foodProvider.getFood())
        
    humanBody : IBody = HumanBody() #no need to pass the parameter here, because the container will provide the dependency       
    humanBody.getHandsQuantity()
    humanBody.eat() #no need to pass the parameter here, because the container will provide the dependency       


If you want to get an instance of an object manually, is possible to use the method *DIContainer.GetObject(IType)*.

