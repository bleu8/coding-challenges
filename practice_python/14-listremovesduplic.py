

#given list 
a = [5, 5, 5, 10, 10, 10, 15, 20, 25]

def remove_duplicates(l):

    return sorted(set(l))

print(remove_duplicates(a))


#%%
def remove_duplicatess(lst):
    x=set(lst)
    return list(x)

y=remove_duplicates([1,1,1,2,2,3,4,5,5,6,7,8])
print(y)


#set te tek eleman olmak zorunda oldugu icin duplicate lardan kurtuluyoruz!!!