#user name validation:


def CodeUsernameVali(s):
    for i in range(2):
        if len(s)>4 and len(s)<25 and s[0].isalpha() and [i for i in s if i.isalnum()  or i=="_"]!=[] and s[-1]!="_":
            return True
        else:
            return False
    
print(CodeUsernameVali(input(">>>>")))
    
    
# alternatif

def CodelandUsernameValidation(str):
  if len(str) < 4 or len(str) > 25 or not str[0].isalpha():
    return "false"
  if str[len(str) - 1] == "_":
    return "false"   #str son karakter _

  for i in str:
    if (not i.isalpha()) and (not i.isdigit()) and (i != "_"):
      return "false"
  # code goes here
  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input(">>>>")))
    
    