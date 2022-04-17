# Create a new list from a two list using the following condition

# Given a two list of numbers, write a program to create a new list such that the 
#new list should contain odd numbers from the first list and even numbers from the second list.

#iki liste lzm tek ve cift olanı anlıyıp ayircaz.

def oorev(l1,l2):
    bos =[]

    
    for i in l1:
        if i%2!=0:
            bos.append(i)
    for j in l2:
        if j%2==0:
            bos.append(j)
            
    return bos
    
    
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(oorev(list1,list2))
