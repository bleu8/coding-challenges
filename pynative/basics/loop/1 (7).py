"""
Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

"""

fakt=1

n=int(input("enter:"))

for i in range(1,n+1):
    fakt=fakt*i
print(fakt)