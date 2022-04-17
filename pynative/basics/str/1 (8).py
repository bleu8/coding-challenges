"""

Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333


"""

def a(str):
    t=0
    ad=0
    for i in str:
        if i.isdigit(): #important
            t+=int(i)
            ad+=1
            avg=t/ad
            
    return t ,avg

print(a("PYnative29@#8496"))