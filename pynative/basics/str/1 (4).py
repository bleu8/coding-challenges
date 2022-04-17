"""


Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output

Dip
Case 2

str2 = "JaSonAy"
Output

Son

"""


def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")