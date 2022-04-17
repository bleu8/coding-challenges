# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

chars=0
sym=0
digit=0
for i in str1:
    if i.isalpha():
        chars+=chars+1
    elif i.isdigit():
        digit+=1
    else:
        sym+=1

    
print("Chars =", chars, "Digits =", digit, "Symbol =", sym)