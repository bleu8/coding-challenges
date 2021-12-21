#question marks:
#https://coderbyte.com/editor/Questions%20Marks:Python3
#olmadi :()
def QuestionsMarks(strParam):
  sorusayac=0
  topla=0
  numkont=False
  for i in strParam:
    if i.isdigit():
      b=int(i)
      if b + topla==10:
        numkont=True
        if sorusayac!=3:
          return False
        topla=b
        sorusayac=0
    elif i =="?":
      sorusayac+=1
    return "false"              
        
                    
            
        
# keep this function call here 
print(QuestionsMarks(input()))
