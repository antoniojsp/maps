example = [{"1":1, "2":2, "3":3, "4":41}, {"1":31, "2":12, "3":31, "4":5}, {"1":1, "2":22, "3":32, "4":6}]


def append_to_end(dictionary, key, item):
    '''
    (dict, str, val)->(dict)
    '''
    temp = dictionary[-1]
    temp[key] = item
    dictionary[-1] = temp
    return dictionary


append_to_end(example, 1)
