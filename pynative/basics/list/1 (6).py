#Exercise 6: Remove empty strings from the list of strings
#withouy filter my sol.
def a(l):
    for i in l:
        if i =="":
            l.remove(i)
            
    return l
            


            
liste=["Mike", "", "Emma", "Kelly", "", "Brad"]
print(a(liste))

#suggested sol.
# =============================================================================
# =============================================================================
# # 
# # list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # 
# # # remove None from list1 and convert result into list
# # res = list(filter(None, list1))
# # print(res)
# # =============================================================================
# 
# =============================================================================
