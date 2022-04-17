# Exercise 9: Check file is empty or not

import os

if os.stat('a.txt').st_size==0:
    print("empty")
else:
    print( "full")

