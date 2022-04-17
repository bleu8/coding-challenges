 #Exercise 4: Remove first n characters from a string


#n' e kadar olanları sil

def remove_chars():
    a=int(input("enter num>>>>"))
    str=input(">>>>>")

    
    if a<len(str):
        print(str[a:len(str)])
          
    else:
        print("girdigin harf saısından kucuk sayi gir!!!!!")

    


# s="istanbul"


remove_chars()
