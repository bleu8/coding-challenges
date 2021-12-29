#max min eleman farkı dondur listeden

def fark(liste):

    max=liste[0]
    min=liste[0]

    for i in liste:
        if i>max:
            max=i
        elif i<min:
            min=i
        return max-min

fark([1,3,7787,332,73,23,-77])

