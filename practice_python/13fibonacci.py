"""

Write a program that asks the user
 how many Fibonnaci numbers to generate and then generates them.
 Take this opportunity to think about how you can use functions. 
 Make sure to ask the user to enter the number of numbers in the sequence to generate.
 (Hint: The Fibonnaci seqence is a sequence of numbers where the next number 
  in the sequence is the sum of the previous two numbers in the sequence.
  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

inp=int(input('How many fibonnaci numbers you want me to generate:\n'))
def fibonnaci(num):
    counter=0
    x=1
    y=0
    while counter<num:
        print(x)
        temp=x
        x+=y
        y=temp
        counter+=1
fibonnaci(inp)



def fibonacci(num):
    a = [0, 1]
    i = 2
    while i < int(num):
        a.append(a[len(a)-2] + a[len(a)-1])
        i += 1
    return a


print(fibonacci(input("How many should I return in fibonacci sequence: ")))