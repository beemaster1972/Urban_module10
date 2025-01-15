import requests


def introspection_info(obj)->dict:
    result={}
    info = dir(obj)
    if '__name__' in info:
        print(obj.__name__)
    print(type(obj))
    print(info)
    print(obj.__dir__())
    # print(obj.__doc__)
    return result


if __name__ == '__main__':
    introspection_info('123')
    introspection_info(123)
    introspection_info(requests)