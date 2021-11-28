a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    

#x=list(set(a).intersection(b)) #buttt we have to lcompr
def intersec(a,b):
    y=[x for x in b if x in a]
    return y

print(intersec(a,b))