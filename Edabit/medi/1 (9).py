# https://edabit.com/challenge/AJGqpNL2yAyhbdpvB


def Dac(num):

    d=(num/1023)*5
    return f"{d:.2f}"

print(Dac(56))