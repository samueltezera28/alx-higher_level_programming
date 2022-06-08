#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    res = 0
    for i in set1:
        res = res + i
    return res