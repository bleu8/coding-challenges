"""

Write a program (using functions!) 
that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.
 For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My


"""

def reverse(txt):
	list1 = txt.split(" ")	# Splits the texts into lists
	list1.reverse()		# Reverses the texts
	new = ' '.join(list1)	# Combines them into one sentences
	return new		# Returns processed text
	
print(reverse(txt = str(input('Input: '))))		
	# Receives string Input while calling the reverse 
	# function using the input parameters and printing
	# the return value at the same time

#%%shorter

text = input("Input the text: ")
print(" ".join(text.split()[::-1]))


#%%more

inp=input('Enter a long string:\n')
#Splits the words in the long string
l=inp.split()

def reverse(x):
    y=len(x)-1
    z=''
    while y>=0:
        z+=(x[y]+" ")
        y-=1
    print(z)

reverse(l)





#split kullanimi -----
dizi = 'python java c'
print(dizi.split())


