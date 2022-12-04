from inspect import isfunction
from typing import get_type_hints

SINGLETON = "SINGLETON"
SCOPED = "SCOPED"

def inject(f):
    def decorator(objectInstance):
        hints = get_type_hints(f)
        params = {}
        keys = hints.keys()
        
        params.update({"self": objectInstance})
        for key in keys:
            if key != "return":
                params.update({key: DIContainer.GetObject(hints[key])})
            
        return f(**params)
    return decorator


class DIContainer(object):
    __objects = {}
    
    @classmethod
    def validateIfTypeExists(cls, typeObject) -> None:
        if typeObject.__name__ in cls.__objects:
            raise Exception(f'Type {typeObject.__name__ } already exists in DIContainer.')
    
    @classmethod
    def AddSingleton(cls, typeObject, typeOrFunction):
        cls.__objects.update({typeObject.__name__ : {"instance":typeOrFunction, "type": SINGLETON, "create": True}})
    
    @classmethod
    def AddScoped(cls, typeObject, typeOrFunction):
        isFunc = type(typeOrFunction).__name__ == "function"
        cls.__objects.update({typeObject.__name__ : {"instance": typeOrFunction, "type": SCOPED, "create": True, isfunction : isFunc}})
    
    @classmethod
    def GetObject(cls, typeObject):
        typeName = typeObject.__name__
        if typeName in cls.__objects:
            obj = cls.__objects[typeName]
            if obj["type"] == SINGLETON:
                if obj["create"]:
                    cls.__objects[typeName]["create"] = False
                    cls.__objects[typeName]["instance"] = cls.__objects[typeName]["instance"]()
                    obj = cls.__objects[typeName]
                return obj["instance"]
            
            return obj["instance"]()
        raise Exception(f'Could not find a instance configured for the type {typeName}')
            
