#iki string birbrinin anagrami mi????


def AnagR(s,j):
    #kelimeleri sozluge cevirelim
    
    if len(s) != len(j):
        return False
    
    s1={}
    s2={}
    
    
    for harf in s:
        if harf not in s1.keys():
            s1[harf]=1
        else:
            s1[harf]+=1
        
        
    for harf in j:
        if harf not in s2.keys():
            s2[harf]=1
        else:
            s2[harf]+=1
            
    return s1==s2


#o'n de calisir verimli!

            