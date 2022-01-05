"""
6.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

b= 3, 5, 7, 23

h=list(b)
t=tuple(b)



def nums():
    num=[]
    l=0
    while l<5:
        n=int(input())
        num.append(n)
        l+=1

    print("Tuple:",tuple(num))
    print("List:",list(num))

print(nums())


#%% other sol:
a=list()
for i in range(5):
    value = input("Please Enter the number: ").split(",")
    a.append(value)
    lst = list(a)
    tple =tuple(a)
print(lst,tple)