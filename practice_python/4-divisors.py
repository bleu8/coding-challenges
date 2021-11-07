def divisors(s):
    divisor=[]
    for i in range(1,s+1):
        if s%i==0:
            divisor.append(i)
    return divisor


print(divisors(35))