#hacker speak
def hacker_speak(sentence):
    alphb={"a":4,"e":3,"i":1,"o":0,"s":5}
    sol=""

    for c in list(sentence):
        try:
            sol+=str(alphb[c])
        except:
            sol+=c
    return sol

print(hacker_speak("java is cool babe"))
