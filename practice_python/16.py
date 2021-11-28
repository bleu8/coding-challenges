import string
import random

    
strings="abcdefghjklmnoprstruvyzxqw"
u_string=strings.upper()

nums="0123456789"
symbol=",.*_-"
topl=strings+u_string+nums+symbol

passl=8


password = "".join(random.sample(topl,passl))

print(password)
#%% shorter alternative 
import string
import random

alphabet = string.ascii_letters

generator = ''.join([random.choices(alphabet)[0] for character in range(8)])

print(generator)



 #fonksiyon alt 2:
import random
import string

def secretGen(n):
    return random.sample(string.ascii_letters + string.digits + string.punctuation, n)

def m():
    n = int(input('input the number of screts you want:'))
    print(''.join(secretGen(n)))


m()