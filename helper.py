def the_best_companion():
    return "Yes"

def sum_list(list1, list2):
    return list1 + list2

def string_helper(string):
    string = string.split(',')
    print(string)

def secret(list):
    for i in range(len(list)):
        list[i] = f'{list[i]} i messed up the line'
    return list

def func():
    print("And I think to myself\n What a wonderful world")

import numpy as np
def numpy_features(a, b, c):
    print(np.roots([a, b, c]))


