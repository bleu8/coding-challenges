a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bos=[]

for i in a:
    if i <5:
        print(i)
        bos.append(i)
print(bos)


#alternative with list comp
result = [x for x in a if x < 5]

print(result)
