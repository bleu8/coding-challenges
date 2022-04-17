# https://edabit.com/challenge/HYjQKDXFfeppcWmLX


import re


def Curzon(a):
    if a**5+1 % a*5+1 ==0:
        return "curzon"
    return "not"


print(Curzon(4))
