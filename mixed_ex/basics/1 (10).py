"""
 31.Write a Python program to compute the greatest common divisor (GCD) of two positive integers
"""
# get 2 num
# for la buyuk olan sayıya kadar gez 1,2,....kendine bolunup bolnmedi

def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd   
print(gcd(13, 17))
print(gcd(180,90))


#%% with libr.
import math
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
gcd_res = math.gcd(num1, num2)
print(f'The greatest common divisor for your numbers {num1} and {num2} is {gcd_res}.')