"""

Exercise 8: Generate a Python list of all the even numbers between 4 to 30
"""  


def a():
    ls=[]
    for i in range(4,31):
        if i %2==0:
            ls.append(i)
    return ls

print(a())