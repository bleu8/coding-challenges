# https://leetcode.com/problems/roman-to-integer/

def roman(s):
    romanlet={"i":1,"v":5,"x":10,"l":50,"c":100,"m":1000,"d":5000}

    res=0

    for  i in range(len(s)):
        if i+1< len(s) and romanlet[s[i]] < romanlet[s[i+1]]:
            res-=romanlet[s[i]]
        else:
            res+=romanlet[s[i]]

    return res

print(roman("mcmxciv"))




