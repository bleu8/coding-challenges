#listdeen tek sayilari alip donduren fonksiyon


def teksayi(liste):
    sayac=0
     

    for i in liste:
        if i %2==1:
            sayac=sayac+i

    return sayac




print(teksayi([1,34,67,12,31,72]))
