#first reverse

def FirstReverse(strParam):
  a=""
  for i in strParam:
    a=i+a

  return a



# keep this function call here 
print(FirstReverse(input()))