def perm(kelime):
    if len(kelime)==1:
        return kelime

    else:
        sonuc=[]

        for idx in range(len(kelime)):
            harf=kelime[idx]
            kalan=kelime[:idx]+kelime[idx+1:] #sag ve sol 

            kalan_perm=perm(kalan)


            for per in kalan_perm:
                sonuc.append(harf+per)

        return sonuc
print(perm("abc"))


#daha kisa cozum--> backtracking
