#Print First 10 natural numbers using while loop
"""i=0
while i<=10:
    print(i)
    i=i+1"""
"""0
1
2
3
4
5
6
7
8
9
10"""
#2.Calculate the sum of all numbers from 1 to a given number
"""a=int(input("enter a number:"))
s=0
for i in range(1, a):
    s=s+i
print(s)"""
"""o/p
enter a number:25
300"""
#3.Write a program to print multiplication table of a given number
"""n=int(input("enter a number:"))
for i in range(0,11):
    print(n,"*",i,"=", n*i ) """
"""o/p:
    enter a number:5
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50"""
#4Display numbers from a list using loop
"""L=[1,2,3,4,5,6]
for i in range(len(L)):
    print(i)"""
"""o/p
0
1
2
3
4
5"""
#5.Count the total number of digits in a number
"""n=input("enter a number:")
c=0
for i in n:
    c+=1
print(c)"""
"""o/p
enter a number:123456
6"""
#6Print list in reverse order using a loop
"""l=[1,2,3,4,5,6]
for i in range(len(l)-1,-1,-1):
    print(l[i], end=" ")"""
"""o/p:
    6 5 4 3 2 1"""
#7.numbers from -10 to -1 using for loopDisplay
"""for i in range(10,0,-1):
    print(i)"""
"""O/p:
10
9
8
7
6
5
4
3
2
1"""
#8.Use else block to display a message “Done” after successful execution of for loop
"""for i in range(0,10,2):
    print(i)
else:
    print("Done")"""
"""o/p:
    0
2
4
6
8
Done"""
#9.Write a program to display all prime numbers within a range
"""lower_value=int(input("enter lower range:"))
upper_value=int(input("enter upper range:"))
for i in range (lower_value, upper_value+1):
    for x in range(2,i):
        if(i%x)==0:
            break
        else:
            print(i)"""
#11.Find the factorial of a given number
"""n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)"""
"""o/p
enter a number:5
120"""
#12.Reverse a given integer number
"""a=input("enter a number:")
for i in len(a):
    print(a"""

#13.Find the sum of the series ⦁	upto⦁	 n terms
"""n=int(input("enter a number:"))
s=0
for i in range(0,n+1):
    s=s+i
print(s)"""
"""o/p
enter a number:5
15"""
#14.Calculate the cube of all numbers from 1 to a given number
"""n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i**3)"""
""" o/p:enter a number:9
1
8
27
64
125
216
343
512
729 """
#15.Use a loop to display elements from a given list present at odd index positions
"""l=[1,5,8,9,6,7,12,15]
for i in range(len(l)):
    if i%2!=0:
        print(l[i])"""
#16.⦁	Name the keyword which helps in writing code involves condition.
#if,else,elif
#17.⦁	Write the syntax of simple if statement.
#if (condition):
#19.	Write a program to check whether a person is eligible for voting or not.
#(accept age from user)
"""n=int(input("enter age:"))
if n>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")"""

"""o/p:enter age:56
eligible for voting
enter age:12
not eligible for voting"""
#20.Write a program to check whether a number entered by user is even or odd.
"""n=int(input("enter a number:"))
if n%2==0:
    print("given number is even")
else:
    print("given number is odd")"""
"""o\penter a number:89
given number is odd"""
#21.	a program Write to check whether a number is divisible by 7 or not.
"""n=int(input("enter a number:"))
if n%7==0:
    print("given number is divisble by 7")
else:
    print("not divisible by 7")"""
"""o/p:
    enter a number:56
given number is divisble by 7"""
#22.	Write a program to display "Hello" if a number entered by user is a multiple of five , 
#otherwise "Bye".
"""n=int(input("enter a number:"))
if n%5==0:
    print("hello")
else:
    print("bye")"""
"""o/p
    enter a number:89
    bye"""
#23Write a program to calculate the electricity bill (accept number of unit from user)
#according to the following criteria :

"""a=int(input("enter units consumed:")) 
if a<=100:
    print("no charge")
elif a>=100 and a<=200:
    print((a-100)*5)
else:
    print(500+(a-200)*10)"""
"""o\p:
    enter units consumed:350
2000"""

#24	Write a program to display the last digit of a number.
#(hint : any number % 10 will return the last digit)
"""n=int(input("enter a number:"))
r=n%10
while n!=0:
    print(r)
    break"""
"""o/p:
    enter a number:25
5"""
#25.Write a program to check whether the last digit of a number( entered by user ) is 
#divisible by 3 or not.
"""n= int(input("enter a number:"))
lastdigit=n%10
if lastdigit%3==0:
    print("last number is divisble by 3", lastdigit)
else:
    print("last number is not divisble by 3", lastdigit)"""
"""o/p
enter a number:456987
last number is not divisble by 3 7"""
#26Write a program to accept percentage from the user and
#display the grade according to the following criteria:
"""m=int(input("enter a number:"))
if m>90:
    print("A")
if m>80 and m<=90:
    print("B")
elif m>=60 and m<=80:
    print("C")
else:
    print("below 60 grade is d")"""
#27Write a program to accept the cost price of a bike and
#display the road tax to be paid according to the following criteria :
"""price=int(input("enter a number"))

if price>100000:
    print("road tax is", (price*15)/100)
if price>50000 and price<=100000:
    print("road tax is",(price*10)/100)
elif price <=50000:
    print("road tax is",(price*5)/100)"""
"""o\p:enter a number30000
road tax is 1500.0"""
    


#28.Write a program to check whether an years is leap year or not.

"""year=int(input("enter a year:"))
if (year%4==0)and (year%100!=0)or(year%400==0):
    print("given year is a leapyear:", year)
else:
    print("given year is not a leapyear:", year)"""
"""o/p:enter a year:2002
given year is not a leapyear: 2002"""

    
#32.Write the output of the following if
"""a = 9
if (a > 5 and a <=10):    
    print("Hello")    
else:    
    print("Bye")
    
o/p:Hello"""
#33.Write the logical expression for the following:
#A is greater than B and C is greater than D
#if a>b and c>d:
#34Statement: set of instructions
#35.Write a program to check whether a number entered is three digit number or not.
"""a=int(input("enter a number"))
if a<1000 and a>99:
      print("given number is 3 digit number")
else:
    print("given number is not 3 digit number")"""


"""o/p:
enter a number25
given number is not 3 digit number
enter a number100
given number is 3 digit number"""




#36.	Write a program to check whether a person is eligible for voting or not.(voting age >=18)
"""n=int(input("enter age:"))
if n>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")"""
"""o/p
enter age:78
eligible for voting"""
#37.	Write a program to check whether a person is senior citizen or not.
"""n=int(input("enter age:"))
if n>=60:
    print("Seniorcitizen")
else:
    print("not seniorcitizen")"""
"""enter age:65
Seniorcitizen
enter age:45
not seniorcitizen"""
#38.	Write a program to find the lowest number out of two numbers excepted from user.
"""n=int(input("enter a number:"))
n1=int(input("enter a number:"))
if n1>n:
    print("n is smaller number", n)
else:
    print("n1 is smaller numbr", n1)"""

"""o\penter a number:67
enter a number:89
n is smaller number 67"""
#39.	Write a program to find the largest number out of two numbers excepted from user.
"""n=int(input("enter a number:"))
n1=int(input("enter a number:"))
if n1>n:
    print("n1 is greater number", n1)
else:
    print("n is greater numbr", n)"""
"""enter a number:78
enter a number:90
n1 is greater number 90"""
#40.	Write a program to check whether a number (accepted from user) is positive or negative.
"""n=int(input("enter a number:"))
if n<0:
    print("given number is negative value:", n)
else:
    print("given number is positive value:", n)"""
"""o/p
enter a number:-1
given number is negative value: -1"""
#41.	Write a program to check whether a number is even or odd.
"""n=int(input("enter a number:"))
if n%2==0:
    print("given number is even", n)
else:
    print("given numberis odd", n)"""
"""o\p
enter a number:67
given numberis odd 67"""
#42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both
"""n=int(input("enter a number:"))
if (n%2==0) and (n%3==0):
    print("given number is divisble by 2 and 3")
else:
    print("given number is not divisble by 2 and 3")"""
"""op
enter a number:18
given number is divisble by 2 and 3"""

#43.Write a program to find the largest number out of three numbers excepted from user.
"""a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>b and a>c:
    print("a is greater:", a)
    if b>c:
        print("b is greater:", b)
else:
    print("c is greter:", c)"""
"""enter a number:8
enter a number:9
enter a number:12
c is greter: 12"""
#44.	Accept the temperature in degree Celsius of water and check
#whether it is boiling or not (boiling point of water in 100 oC.
"""temp=int(input("enter temperature:"))
if temp>100:
    print(" temperature of water is at boiling point")
else:
    print("temperature of water is not at boiling point")"""
"""o/p:
enter temperature:101
 temperature of water is at boiling point"""

#45.Accept the age of 4 people and display the youngest one and oldest one?
"""a=int(input("enter age of a:"))
b=int(input("enter age of b:"))
c=int(input("enter age of c:"))
d=int(input("enter age of d:"))
if a>b and a>c and a>d:#a is greater
    print("a is oldest:" ,a)
elif b>a and b>c and b>d:
    print("b is old" , b)
elif c>a and c>b and c>d:
    print("cis old",c)
else:
    print("d is oldest")
if a<b and a<c and a<d:
    print("a is young")
elif b<a and b<c and b<d:
    print("b is young")
elif c<a and c<b and c<d:
    print(c, "is young")
else:
    print(d, "is young")"""
"""o/p:enter age of a:5
enter age of b:65
enter age of c:35
enter age of d:2
b is old 65
2 is young"""
#46.Accept the following from the user and calculate the percentage of class attended:
"""total_days=int(input("enter total number of working days:"))
days_absent=int(input("enter  number of days absent:"))
present=(total_days-days_absent)
per=(present/total_days)*100
if per<75:
    print("not eligible to sit in the exam")
else:
    print("eligible for exam")"""
"""enter total number of working days:100
enter  number of days absent:5
eligible for exam
enter total number of working days:50
enter  number of days absent:25
not eligible to sit in the exam"""    

#47.Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
"""side_1=int(input("enter a side one"))
side_2=int(input("enter side two:"))
side_3=int(input("enter side three:"))
if side_1==side_2==side_3:
    print("triangle is equilateral")
if side_1==side_2 and side_2!=side_3:
    print("triangle is isosceles")
elif side_1!=side_2 and side_2!=side_3:
    print("triangle is scalene")"""
"""o/p:
enter a side one5
enter side two:5
enter side three:2
triangle is isosceles"""
#29Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
"""day =int(input("Enter day : "))
if day == 1 :
    print("Monday");

elif day == 2 :
    print("Tuesday")

elif(day == 3) :
    print("Wednesday")

elif(day == 4) :
    print("Thursday")

elif(day == 5) :
    print("Friday")

elif(day == 6) :
    print("Saturday")

elif (day == 7) :
    print("Sunday")

else :
    print("Please enter any weekday number (1-7)")"""
"""o/p:
    Enter day : 8
Please enter any weekday number (1-7)"""
#30.to accept a number from 1 to 12 and display name of the month and days
#in that month like 1 for January and number of days 31 and so on
"""num =int(input("Enter a number : "))
if num==1:
    print("January, Number of Days: 31")
elif num==2:
    print("February, Numer of days: 28")
elif num==3:
    print("March, Numer of days: 31")
elif num==4:
    print("April, Numer of days: 30")
elif num==5:
    print("May, Numer of days: 31")
elif num==6:
    print("June, Numer of days: 30")
elif num==7:
    print("July, Numer of days: 31")
elif num==8:
    print("August, Numer of days: 31")
elif num==9:
    print("September, Numer of days: 30")
elif num==10:
    print("October, Numer of days: 31")
elif num==11:
    print("November, Numer of days: 30")
elif num==12:
    print("December, Numer of days: 31")
else:
    print("Please enter a number from (1-12)")"""
"""o/p:
    Enter a number : 6
June, Numer of days: 30
Enter a number : 13
Please enter a number from (1-12)"""
#33⦁Accept any city from the user and display monument of that city.
"""city=input("enter a city name:")
if city=="Delhi":
    print("Visit Redfort")
elif city=="agra":
    print("Visit Tajmahal")
elif city==" Jaipur":
    print("Visit jalmahal")
else:
    print("Please enter cities Agra, Delhi, Jaipur")"""

"""o/p:enter a city name:orissa
Please enter cities Agra, Delhi, Jaipur
enter a city name:agra
Visit Tajmahal"""
    
