def get_sub_object_from_path(dict_name, map_list):
    for i in map_list:
        _string = "['%s']" % i
        dict_name += _string
    value = eval(dict_name)
    return value

if __name__ == '__main__':
    #Enter the dict values 3 keys and 1 values, put all values in new line
    _dict = {input(): {input(): {input(): input()}}}
    #Enter the keys of which you want to get the values, in "key1/key2/.. format"
    keys = [item for item in input().split('/')]
    print(get_sub_object_from_path("_dict", keys))