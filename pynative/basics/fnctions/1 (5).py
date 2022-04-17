"""
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself, again and again.

"""



def rec_s(num):
    if num:
        return num+rec_s(num-1)

    else:
        return 0
res=rec_s(10)