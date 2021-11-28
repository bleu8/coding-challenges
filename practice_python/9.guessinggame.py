"""
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""
#%%
# =============================================================================
# import random 
# 
# a=random.randint(0,10)
# cond=1
# while cond:
#     user=int(input("guess a number"))
#     
#     if user <a:
#         print("up")
#     elif user>a:
#         print("down")
#         
#     else:
#         print("conguralitons!!!")
#         break
#         
#         
# =============================================================================
    
#%%functions 

import random
int1 = random.randint(0,9)
int2 = int(input("Enter a random number between 0 to 9"))
print("The random number is {}".format(int1))

def compare(n1, n2):
    if n1 == n2:
        return("You guessed right")
    elif n2 > n1:
        return("Your guessed number is greater than the actual number!")
    else:
        return("Your guessed number is less than the actual number!")

print(compare(int1,int2))