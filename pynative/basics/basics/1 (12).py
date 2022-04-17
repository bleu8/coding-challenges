#Exercise 11: Write a Program to extract each digit from an integer in the reverse order


#for la liste uzerinde elemanlarda gezebilriiz bos bi listeya aktrp basabiliriz :/


empty=""
num=6457
for i in str(num):
    empty=i+empty #strye donusum
m=list(empty) #list'e donusum:
print(m)
    



    
# =============================================================================
# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")
# =============================================================================

