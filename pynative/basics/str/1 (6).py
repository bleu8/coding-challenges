"""

Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive
Expected Output:

yaivePNT

"""
lower =[]
upper=[]
str1 = "PyNaTive"
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)



sorted_st="".join(lower+upper)
print(sorted_st)
