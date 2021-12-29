#Exercise 6: Display numbers divisible by 5 from a list

def divis(l):
    for i in l:
        if i%5==0:
            print(i)
            return "divisible by 5"
            
        return "false"
    
print(divis([5,8,9,80,55]))

