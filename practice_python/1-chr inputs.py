# name =input("name>>>")
# age=int(input("age>>>"))
# year=2021+(100-age)

# print(name+ " " +str(age)+" " +str(year))


#with date time modulu
import datetime

now = datetime.datetime.now()
currentyear = now.year
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
hundredIn = ((100 - age) + currentyear)

print ('Hi '+name + ', you will be 100 years old in ' + str(hundredIn))