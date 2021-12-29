def ciftCarp(liste):
    carpım=1

    for i in liste:
        if i %2==0:
            carpım*=i
    
    return carpım

print(ciftCarp([1,4,57,338,931,2]));