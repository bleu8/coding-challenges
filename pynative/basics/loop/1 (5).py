"""

Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.


"""
i=0
num=int(input(">>>>>"))
counter=0
while i<len(str(num)):
    counter+=1
    i+=1
print(counter)

# =============================================================================
# #more efficent 
# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10
# 
#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)
# 
# =============================================================================
