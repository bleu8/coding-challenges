# Create a function with variable length of arguments



def f(*args):
    for i in args:
        print(i)


f(90,45,6,7)