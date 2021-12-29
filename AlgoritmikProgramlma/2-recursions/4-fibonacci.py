#recursive 
def fib(a):
   
   # fib(0)=0 fib(1)=1 en alt kısım


    if a==0 or a==1:
            return a
    else:
        return fib(a-1)+fib(a-2)

#ozyinelemeli kısım fn= fn-1 +fn-2


fib(3)