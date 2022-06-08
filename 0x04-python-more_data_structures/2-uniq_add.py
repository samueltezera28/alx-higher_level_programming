#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    result = 0
    for i in set1:
        result = result + i
    return [result]