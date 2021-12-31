#Write a program to create a new string made of an input string’s first, middle, and last character.

str="istanbul"

g=int(len(str)/2)

print(str[0]+str[g]+str[-1])


#%%

str1 = 'istanbul'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)