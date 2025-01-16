import requests
import inspect
from pprint import pprint


class MyClass:
    CLASS_VAR = 100

    def __init__(self):
        self.a = 1
        self. b = 2

    def my_method(self)->bool:
        return True

def introspection_info(obj) -> dict:
    result = {}
    result['info'] = [el for el in dir(obj) if not el.startswith('_')]
    if hasattr(obj,'__name__'):
        result['name'] = obj.__name__
    # print(type(obj))
    result['type'] = type(obj)
    if hasattr(obj,'__dict__'):
        result['attr'] = [el for el in list(obj.__dict__.keys()) if not el.startswith('_')]
    result['methods'] = inspect.getmembers(obj,predicate=inspect.isfunction)
    result['module'] = inspect.getmodule(obj)
    if hasattr(obj,'__doc__'):
        result['doc'] = obj.__doc__

    # print(info)
    # print(obj.__dir__())
    #print(obj.__doc__)
    return result


if __name__ == '__main__':
    pprint('String')
    pprint(introspection_info('123'))
    pprint('Int')
    pprint(introspection_info(123))
    pprint('requests')
    pprint(introspection_info(requests))
    pprint('MyClass')
    my_class = MyClass()
    pprint(introspection_info(MyClass))
    pprint(introspection_info(my_class))
