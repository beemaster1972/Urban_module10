def introspection_info(obj)->dict:
    result={}
    # print(obj.__name__)
    print(type(obj))
    print(dir(obj))
    print(obj.__doc__)
    return result


if __name__ == '__main__':
    introspection_info('123')