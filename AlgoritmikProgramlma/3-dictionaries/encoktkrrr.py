#En cok tekrar eden harf


def n_cok(s):
    sl={} #stringi bos bir sozlukte tutmak gerekcek!
    maxi=0
    son=""
    for harf in s: #str
        if harf not in sl.keys(): #dict
            sl[harf]=1
        else:
            sl[harf]+=1
    for key,val in sl.items():
        if val>maxi:
            son=key
            maxi=val
    return son
                    
            