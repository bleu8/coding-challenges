#Exercise 5: Check if the first and last number of a list is the same

#list ac istedhgin sayi adedi for ile acabiliriz.
#for ile 
#butun elemanlari gecersek son ve bas kiyaslamak icin 


# =============================================================================
#Example:
# # Given list: [10, 20, 30, 40, 10]
# # result is True
# 
# # numbers_y = [75, 65, 35, 75, 30]
# # result is False
# =============================================================================



def firstnlast(c):
    for i in c:
        if c[0] == c[len(c)-1]:
            return "yes"
        return "no"



print(firstnlast([1,43,6,10,1]))         