#intersection

 #https://coderbyte.com/editor/Find%20Intersection:Python3
 
 
#my code

def intersect(strArr):
    s1=set(strArr[0].split(","))
    s2=set(strArr[1].split(","))

  
    a=s1.intersection(s2)


    return a




 #return the strr of num fond in both in sorted order
 #retun false if there s no intersection

#bunlar icinde liste barindiran array indexlenebilir.ve ayrilabilir.set haline alip intersect metoduyla ayirabiliriz.!
print(intersect(["2,3,5,78,","4,2,6,78"]))


#but better ones:
def FindIntersection(strArr):
  a = map(int, strArr[0].split(', '))
  b = map(int, strArr[1].split(', '))
  c = list(set(a) & set(b))
  c.sort()
  return ','.join(map(str, c))

print(FindIntersection(input()))



