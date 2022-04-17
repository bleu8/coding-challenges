#Write a program to find how many times substring “Emma” appears in the given string.
# 28 december 



def FindStr(v):
   cnt=v.count("Emma")
   return cnt
    
print(FindStr("I like Emma Stone movies with my friend Emma"))

#%%more like a programmer:
def count_emma(stri):
    count=0
    for i in range(len(stri)):
        count+=stri[i:i+4] =='Emma'
    return count


print(count_emma("i love you Emma watson i'm Emma"))