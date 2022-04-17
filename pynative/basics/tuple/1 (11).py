# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222


tuple1 = (11, [22, 33], 44, 55)

l=list(tuple1)

l[1][0]=222
l[1][1]=333
a=tuple(l)