
def top_rec(n):

    if n==1:  #taban vaka
        return 1
    else:
        return top_rec(n-1)+n

top_rec(3)