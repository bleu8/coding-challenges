# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

#So cool
import random

def create_list():
    a = random.randint(0,99)
    liste = list(range(1, a+1))
    return liste

def first_last(a):
    first_last = []
    first_last.extend([a[0], a[-1]])
    print(first_last)
    
first_last(create_list())
#%%
#
#given list 
a = [5, 10, 15, 20, 25]

def new_list(i):
    print([i[0],i[len(a)-1]])

new_list(a)

#Shorter!!
a=[int(x) for x in input('Enter the numbers\n').split()]
i=0
j=len(a)
print(a[i],a[j-1])