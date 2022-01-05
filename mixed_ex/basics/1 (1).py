"""

7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""


def k(a):
    count=0
    for i in a:
        if i==".":
            count+=1
            return a[count:]



b=input(" file>>>>")
print(k(b))

"""

easier thn mine:

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


"""

#detailed for repr--< https://www.programiz.com/python-programming/methods/built-in/repr