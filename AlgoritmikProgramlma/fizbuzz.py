def fizzbuz(n):
    for i in range (n+1):
        if i%15==0:
            print("Fizzbuzz")
            
        elif i%5==0:
            print("buzz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)
    
    
    
    
a=int(input("gir>>>"))
print(fizzbuz(a))