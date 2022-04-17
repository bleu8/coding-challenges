# Exercise 16: Removal all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'
# Expected Output:

# 2510

str2 = "I am 25 years and 10 months old"
dig=[]

res = "".join([item for item in str2 if item.isdigit()])

print(res)