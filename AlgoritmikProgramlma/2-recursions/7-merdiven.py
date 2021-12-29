# #bir cocuk n basamaklı merdiven çıkmak istiyor
# 1,2,veya 3 basamak cıkıyor basamakları
#  kac farklı sekilde yapabilir?

memo={}

def bas(n):

    if n<1:
        return 0
    if n==1 or n==2:
        return n
    elif n==3:
        return 4


    elif n in memo.keys():
        return memo[n]
    else:
        memo[n]=bas[n-1]+bas[n-2]+bas[n-3]
        return memo[n]