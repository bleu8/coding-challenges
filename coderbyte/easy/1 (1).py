#  #with regex

# import re
# pattern = re.compile(r'\W+')
# def LongestWord(sen): 
#     x = pattern.split(sen)
#     return max(x, key=len)


# print(LongestWord(input()))



# def long(s):
#     bos=""
#     for i in s:
#         if i.isalpha() or i.isnumeric():
#             bos+=i
#         else:
#              bos+=""
#     return max(bos.split(),key=len)

# print(long("istanbulankaraizmir"))

   #https://coderbyte.com/information/Longest%20Word

#our solution:
def lh(k):
    max=0
    
    for i in k.split():
        if len(i)>max and i.isalpha():

            max=len(i)
            large=i

    return large



print(lh("i love istanbul"))
