# Exercise 10: Check if all items in the tuple are the same
#!!!

tuple1 = (45, 45, 45, 45)



tuple1 = (45, 45, 45, 45)
if len(set(tuple1)) == 1:
    print(True)
    
    
tuple1 = (45, 45, 45, 45)
tuple2 = tuple1[::-1] #reverse 
if tuple1 == tuple2:
    print("True")
else:
    print("False")
    
#other sol.
tuple1 = (45, 45, 45, 45)
print(min(tuple1) == max(tuple1))