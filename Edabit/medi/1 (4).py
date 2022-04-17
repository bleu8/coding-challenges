# https://edabit.com/challenge/WXqH9qvvGkmx4dMvp


def FizzzBuzz(a):

    if a%15==0:
        return "fizzbuzz"
    elif a %5==0:
        return "fizz"
    elif a% 3==0:
        return "buzz"


print(FizzzBuzz(30))