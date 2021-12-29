#memory acısından cok iyi degil dynamic programming

def fiba(n):

    if n==0:
        return 0
    r=1
    l=0
    
    for i in range(1,n):

        l,r=r,r+l 
    return r


