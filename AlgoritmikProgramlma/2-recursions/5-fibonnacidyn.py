#dynamic programming

memo={}

#recursive 
def fib(a):
   
   # fib(0)=0 fib(1)=1 en alt kısım


    if a==0 or a==1:
            return a

    if a not in memo.keys():
        memo[a]=fib(a-1)+fib(a-2)

    return memo[a]

fib(3)