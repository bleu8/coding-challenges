"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

#our shitty code: :/ 
i=input("enter>>>>")

wovel="a","e","u","i","o"

if i in wovel:
    print("vovel")
else:
    print("not")
        
#%% 
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


#%% shorter!
letter = input('Please enter ')


if letter in 'aeiou':
    print('The letter is a vowel!')
else:
    print('The letter is not a vowel.')
    
 #%%
import re
c=input("enter>>>>")

if re.match("[aeiou]",c):
    print( "wovel")
else:
    print("not")
    
