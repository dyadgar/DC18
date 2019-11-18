import datetime

print()


# print(cake)


# birthdate= datetime(input("Write your date of birth DD/MM/YYYY "))

# print(birthdate)

year= int(input("What year were you born"))
month= int(input("What month were you born "))
day= int(input("What day were you born"))

date1= [day,month,year]


print(date1)
print(date1[2])

yearstr=str(date1[2])
print(type(yearstr))

yearChar=yearstr[3];
yearInt=int(yearChar)
print(type(yearInt))

candles= (yearInt) * "i"
spaces= (yearInt) * "_"


cake = ("	__"+spaces+candles+spaces+"__" '''     
     |:H:a:p:p:y:|
   __|___________|__
  |^^^^^^^^^^^^^^^^^|
  |:B:i:r:t:h:d:a:y:|
  |                 |
  ~~~~~~~~~~~~~~~~~~~
       
\n


''')


if(year %4 is 0):
	print(cake*2)
else:
	print(cake)
# print(f'''\t\t{candles}       
# \t	   ___________
# \t      |:H:a:p:p:y:|
# \t    __|___________|__
# \t   |^^^^^^^^^^^^^^^^^|
# \t   |:B:i:r:t:h:d:a:y:|
# \t   |                 |
# \t   ~~~~~~~~~~~~~~~~~~~''')


