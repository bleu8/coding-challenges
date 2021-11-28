#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html


#prime or not


def Prime(a):
    for i in range(2,a+1):#mantik su sayiyi 2den baslıyip kendisine kadar bolumunu denersek eger bolunurse asal degildir.
        if a%i==0:
            return "not prime"
        else:
            return "prime"
        
t=int(input("pls number"))
print(Prime(t))



#lets see other's solutions

num=int(input("number>>>>>"))

myl=[x for x in range(2,num-1) if num%x==0]  #list comprehension

def isPr(num):
    if len(myl)==0:
        return "prime"
    else:
        return "not"
    
print(isPr(34))