"""
 Write a Python program to
 get a string which is
 n (non-negative integer) 
 copies of a given string

"""
#my sol.
s=input()
n=int(input("number>>>>"))

a=s*n
print(a)


#fnc:
def copy(a,n):
    if n>0:
        return(a*n)
    

#%%
#longer other's sol.
def calc(k,n):
   
   for i in range(n):
    m=""
    m=m+k
    print(m)
calc(input('enter string'),int(input('number of copies')));