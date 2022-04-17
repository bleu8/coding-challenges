# https://edabit.com/challenge/Ns4Sjh7KK58ofAph8

from  math import sqrt
def Pythagor_triplet(a,b,c):
    if a==sqrt(b^2+c^2) or b ==sqrt(a^2+c^2) or c==sqrt(a^2+b^2):
        return "yes"
    return "no"

print(Pythagor_triplet(3,4,5))
