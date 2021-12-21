#first factorial--> 

#this is o(n) sol:
def fact(num):
	if num==0:
		return 1
	f=1
	for i in range(1,num+1):
		f=f*i

	return f 

print(fact(6))


#liked other's solution---< with math library.>
#1

from math import factorial

def FirstFactorial(num): 

  # code goes here 
  # Note: don't forget to properly indent in Python

  return factorial(num)
    

print(FirstFactorial(6))


#recursive:
def fc(n):
    if n==1 or n==0:
        return 1
    return fc(n-1)*n
 
print(fc(3))
    
