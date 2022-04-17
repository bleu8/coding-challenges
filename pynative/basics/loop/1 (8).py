"""

Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567

"""


num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10  #last 
    reverse_number = (reverse_number * 10) + reminder  
    num = num // 10
print("Revere Number ", reverse_number)