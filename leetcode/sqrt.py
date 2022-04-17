
# # in a straight way: :D
# class Solution(object):
#     def mySqrt(self, x):
#         return int(sqrt(x))


def mysqrt(x):
    start = 0
    while(True):
        if (start * start > x):
            return start - 1
        else:
            start += 1

print(mysqrt(4))