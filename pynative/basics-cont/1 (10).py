#Check Palindrome Number

#number str ye cevrilip bakibilir forla uzerinde gezerek
# =============================================================================

#example:
# original number 121
# Yes. given number is palindrome number
# 
# original number 125
# No. given number is not palindrome number
# =============================================================================

# bos=""
# num=int(input(">>>>>"))
# for i in str(num):
#     bos+=i
#     if bos==num:
#         print("yes")
#     else:
#         print("no")
        
        
num=input(">>>>>")
        
if num[::-1]==num:
    print("yes")
else:
    print("no")
