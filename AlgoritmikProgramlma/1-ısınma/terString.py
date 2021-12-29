def tersAl(s):


    #stringler immuatble bu yuzden bos str'ye atıp yapmaliyiz

    ters=""

    for i in s:
        ters=i+ters

    return ters

print(tersAl("ali"))


"""
#daha kısası

def ters(s1):  #index 0dan basladıgı icin  geriye sayıcaz son indexten basa kadar 0 dahil degl -1 yazdık
    for i in range(len(s1)-1,-1,-1):
        print(s1[i],end="")

ters("ali")
"""



#%%en kisasi python 2 cozumu
"""
def tersle(s):
    return s[::-1]
print(tersle("ali"))

#bu maniplation stringte de oluyor!"""