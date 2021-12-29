#iteratif yolla

def fac(n):

    fact=1

    for i in range(1,n+1):

        fact=i*fact

    return fact


fac(3)

#recursive
#baz vaka


def fac_rec(h):
    #taban durumu 
    if h==0:
        return 1
    
    else:
        return fac_rec(h-1)*h
    
    