import unittest
from PyDInjector import DIContainer
from PyDInjector.test.data.classes.Cooker import Cooker
from PyDInjector.test.data.classes.FoodProvider import FoodProvider
from PyDInjector.test.data.interfaces.IBody import IBody
from PyDInjector.test.data.interfaces.IBodyAction import IBodyAction
from PyDInjector.test.data.classes.HumanBody import HumanBody
from PyDInjector.test.data.classes.HumanBodyAction import HumanBodyAction
from PyDInjector.test.data.interfaces.ICooker import ICooker
from PyDInjector.test.data.interfaces.IFood import IFoodProvider

class TestScopedInjection(unittest.TestCase):
    
    def setUp(self):
        DIContainer.AddScoped(IBody, HumanBody)
        DIContainer.AddScoped(IBodyAction, HumanBodyAction)
        DIContainer.AddScoped(IFoodProvider, FoodProvider)
        DIContainer.AddScoped(ICooker, Cooker)
             
    def test_create_instance(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.getHandsQuantity(), 2)
        self.assertEqual(humanBody.getLegsQuantity(), 2)
    
    def test_inject_and_use_injected_object(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.jump(), 'jumped')        
        self.assertEqual(humanBody.move(), 'moved')        
    
    def test_inject_many_instances(self):
        humanBody1 : IBody = HumanBody()
        humanBody2 : IBody = HumanBody()
        id1 = humanBody1.getInstanceIdentification() 
        id2 = humanBody2.getInstanceIdentification()
        self.assertNotEqual(id1, id2)
        self.assertEqual(id1, humanBody1.getInstanceIdentification())
        self.assertEqual(id2, humanBody2.getInstanceIdentification())

        id1Action = humanBody1.getActionIdentification() 
        id2Action = humanBody2.getActionIdentification()
        self.assertIsNotNone(id1Action)
        self.assertIsNotNone(id2Action)
        self.assertNotEqual(id1Action, id2Action)
        self.assertEqual(id1Action, humanBody1.getActionIdentification())
        self.assertEqual(id2Action, humanBody2.getActionIdentification())

    def test_inject_method_scoped(self):
        humanBody1 : IBody = HumanBody()
        food1 = humanBody1.eat()
        food2 = humanBody1.eat()
        food3 = humanBody1.eat()
        self.assertEqual(food1, 'Meat')
        self.assertEqual(food2, 'Meat')
        self.assertEqual(food3, 'Meat')
    
    def test_inject_multiple_instances(self):
        cooker = Cooker()
        foods = cooker.getFoods()
        self.assertEqual(foods[0].getFoodName(), 'Meat')
        self.assertEqual(foods[1].getFoodName(), 'Meat')        


class TestSingletonInjection(unittest.TestCase):
    
    def setUp(self):
        DIContainer.AddSingleton(IBody, HumanBody)
        DIContainer.AddSingleton(IBodyAction, HumanBodyAction)
        DIContainer.AddSingleton(IFoodProvider, FoodProvider)
        DIContainer.AddSingleton(ICooker, Cooker)
             
    def test_create_instance(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.getHandsQuantity(), 2)
        self.assertEqual(humanBody.getLegsQuantity(), 2)
    
    def test_inject_and_use_injected_object(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.jump(), 'jumped')        
        self.assertEqual(humanBody.move(), 'moved')        
    
    def test_inject_many_instances(self):
        humanBody1 : IBody = HumanBody()
        humanBody2 : IBody = HumanBody()
        id1 = humanBody1.getInstanceIdentification() 
        id2 = humanBody2.getInstanceIdentification()
        self.assertNotEqual(id1, id2)
        self.assertEqual(id1, humanBody1.getInstanceIdentification())
        self.assertEqual(id2, humanBody2.getInstanceIdentification())

        id1Action = humanBody1.getActionIdentification() 
        id2Action = humanBody2.getActionIdentification()
        self.assertIsNotNone(id1Action)
        self.assertIsNotNone(id2Action)
        self.assertEqual(id1Action, id2Action)
        self.assertEqual(id1Action, humanBody1.getActionIdentification())
        self.assertEqual(id2Action, humanBody2.getActionIdentification())

    def test_inject_method_scoped(self):
        humanBody1 : IBody = HumanBody()
        food1 = humanBody1.eat()
        food2 = humanBody1.eat()
        food3 = humanBody1.eat()
        self.assertEqual(food1, 'Meat')
        self.assertEqual(food2, 'Pasta')
        self.assertEqual(food3, 'Rice')
    
    def test_inject_multiple_instances(self):
        cooker = Cooker()
        foods = cooker.getFoods()
        self.assertEqual(foods[0].getFoodName(), 'Meat')
        self.assertEqual(foods[1].getFoodName(), 'Pasta')

class TestSingletonInjectionUsingFunction(unittest.TestCase):
    def setUp(self):
        DIContainer.AddSingleton(IBody, HumanBody)
        DIContainer.AddSingleton(IBodyAction, lambda : HumanBodyAction())
        DIContainer.AddSingleton(IFoodProvider, FoodProvider)
        DIContainer.AddSingleton(ICooker, Cooker)

    def test_create_instance(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.getHandsQuantity(), 2)
        self.assertEqual(humanBody.getLegsQuantity(), 2)
    
    def test_inject_and_use_injected_object(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.jump(), 'jumped')        
        self.assertEqual(humanBody.move(), 'moved')    
            
class TestScopedInjectionUsingFunction(unittest.TestCase):
    def setUp(self):
        DIContainer.AddScoped(IBody, HumanBody)
        DIContainer.AddScoped(IBodyAction, lambda : HumanBodyAction())
        DIContainer.AddScoped(IFoodProvider, FoodProvider)
        DIContainer.AddScoped(ICooker, Cooker)

    def test_create_instance(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.getHandsQuantity(), 2)
        self.assertEqual(humanBody.getLegsQuantity(), 2)
    
    def test_inject_and_use_injected_object(self):
        humanBody : IBody = HumanBody()
        self.assertEqual(humanBody.jump(), 'jumped')        
        self.assertEqual(humanBody.move(), 'moved')   

if __name__ == '__main__':
    unittest.main()
