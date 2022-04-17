# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. 
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n=5
start=2
sq=0

for i in range(0,n):
    print(start,end="+")
    sq+=start
    start=start*10+2

print(sq)