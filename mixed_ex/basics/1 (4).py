"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

"""


from datetime import date
dt1=date(2014, 7, 2)
dt2=date(2014, 7, 11)
delta=dt2-dt1
print(delta.days)   

#%%

from datetime import date
x,y=date(2022,2,9),date(2019,6,2)
print(x-y)

#%%other:
first = 2,2,1900
second = 11,7,2020
days = second[0] - first[0]
month = (second[1] - first[1]) *30
year = (second[2] - first[2]) * 365
print(days + month + year ,"days")

#https://www.w3resource.com/python-exercises/python-basic-exercise-14.php