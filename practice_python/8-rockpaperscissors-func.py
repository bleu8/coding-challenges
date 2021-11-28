win=["r","p","s","p"]

def RPS():
    
    i1=input("r/p/s>>>> ")
    print(" ")
    i2=input("r/p/s>>>>")
    
    
    if i1==i2:
        return "tie!"
    elif win[win.index(i1)+1==i2]:
        return "win"
    else:
        return "beat"
    
    
while True:
    a=input("yes or no???")
    if a=="yes":
        print(RPS())
    else:
        break