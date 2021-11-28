#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#my terrible code :/


#little touch and shorter
play=True
skorm=0
skorp=0
import random
liste=["rock","scissors","paper"]
pc=random.choice(liste)

while play:
    a=input("choice?>>>")
    if (a=="rock" and pc=="scissors")or (a=="scissors" and pc=="paper") or (a=="paper" and pc=="rock"):
        print("you win")
        skorm+=1 
        print(f" skore for pc>>>{skorp} score for you>>>{skorm}")
    elif (pc=="rock" and a=="scissors")or (pc=="scissors" and a=="paper") or (pc=="paper" and a=="rock"):
        print("pc win")
        skorp+=1
        print(f"scores for pc>>>{skorp} score for you>>>{skorm}")
    elif pc==a:
        print("equal")
        skorm+=1
        skorp+=1
        print(f"scores for pc>>>{skorp} score for you>>>{skorm}")
   

    
    print("continue??")

    x=input()
    if x=="yes":
        play==True
    else:
        break

