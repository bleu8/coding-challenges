#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

#shortcut !!!!
string=input("Enter>>>")


pal=string[::-1]

if pal==string:
    print("It's palindrome!!")
else:
    print( "Not palindrome")


#alternative

x=input('Enter a string to check if it is palindrome or not:\n')
y=''
for k in reversed(x):
    y+=k
if y.lower()==x.lower():
    print('It is palindrome')
else:
    print('It is not palindrome')

