#1Write a program to find sum of number"

"""num1=int(input("Enter a number1:"))# sum of series of number
s=0
for i in range(num1+1):
    s+=i
print("sum of number is:" , s)
o/p:
    Enter a number1:5
sum of number is: 15"""
"""num1=input("Enter a number1:")#sum of number
s=0
for i in num1:
    s+=int(i)
print(s)"""
"""o/p
Enter a number1:25
7"""
#2python program to find strongnumber
n=input("enter a number:")
fact=1
for i in n:
    fact=fact*i
print(fact)
if s==n:
    print("given number is strong", n)
else:
    print("given number is not strong number", n )
    

#3.Python Program to Find the Square Root
"""n=int(input("enter a number:" ))
s=n**0.5
print(s)"""
"""enter a number:49
7.0"""
#4.Python Program to Calculate the Area of a Triangle
"""a=float(input("enter a first side:", ))
b=float(input("enter a second side:", ))
c=float(input("enter a third side:", ))
p= (a+b+c)/2 #perimeter
area=(p*(p-a)*(p-b)*(p-c))**0.5
print("area of a triangle=", area)"""
"""o/p
enter a first side:8
enter a second side:9
enter a third side:6
area of a triangle= 23.525252389719434"""


#6.Python Program to Swap Two Variables
"""num1=input("enter a number:")
num2=input("enter a number:")
print("num1 , num2 before swapping:",  num1, num2)
temp=num1
num1=num2
num2=temp

print("num1 , num2 after swapping:",   num1, num2)
enter a number:12
enter a number:13
num1 , num2 before swapping: 12 13
num1 , num2 after swapping: 13 12"""

#7.Python Program to Convert Kilometres to Miles
"""km=float(input("Enter Kilometers:"))
miles=km*0.621371
print("kiloMeter after conversion into miles:", miles)"""
"""o/p
Enter Kilometers:25
kiloMeter after conversion into miles: 15.534275000000001"""

#8.Python Program to Check Leap Year
"""year=int(input("enter a year:"))
if (year%4==0)and (year%100!=0)or(year%400==0):
    print("given year is a leapyear:", year)
else:
    print("given year is not a leapyear:", year)

o/p enter a year:2000
given year is a leapyear: 2000
enter a year:2022
given year is not a leapyear:2022"""

#9.primenumber
"""n=int(input("enter a given number:"))
factors=[]
for i in range(1,n+1):
    if (n%i==0):
        factors.append(i)
if len(factors)==2:
    print("given number is prime:" n)
else:
    print("given number is not prime" n)"""
"""o/penter a given number:49
given number is not prime49

enter a given number:17
given number is prime:17"""


#10.factorial
"""n=int(input("enter a number:"))
fact=1
for i in range (1,n+1):
    fact= fact*i
print("factorial of a given number is:")"""
"""o\p:
enter a number:5
factorial of a given number is : 120"""  
#11.Fibonacci sequence
"""def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2) 
n=[fibonacci_of(n) for n in range(15)
print(n)"""
"""o/p
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]"""
#12.amstrongnumber
"""n=int(input("enter a number:"))
l=len(str(n))
s = 0
temp = int(n)
while temp > 0:
    digit = temp % 10
    s += digit ** l
    temp //= 10
if n==s:
    print("given number is Armstrong:",n )
else:
    print("given number is not Armstrong:", n)"""
"""O/p
enter a number:153
given number is Armstrong: 153
enter a number:139
given number is not Armstrong: 139"""
#13.Amstrong Number in an interval
       
"""lower = int(input("enter a lower range:", ))
upper = int(input("enter a upper range:", ))

for num in range(lower, upper+1 ):
    l = len(str(num))
    s = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       s += digit ** l
       temp //= 10
       if num == s:
           print(num)"""

"""o/p
enter a lower range:200
enter a upper range:500
216
370
371
407"""
#14.sum of natural numbers
"""n=int(input("enter a number:"))
s=0
for i in range(n+1):
    s+=i
print("sum of numbers is:" , s)"""
"""o\p
enter a number:9
the sum is 45"""

#15.factors of number
"""n=int(input("enter a given number:"))
factors=[]
for i in range(1,n+1):
    if (n%i==0):
        factors.append(i)
print("factors of given number", factors)"""
"""o/penter a given number:25
factors of given number [1, 5, 25]"""




#17python Program to Find LCM
"""def calculate_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm = greater
            break
        greater+=1
    return lcm
print("The LCM of 54 and 24 is", calculate_lcm(54,24))"""
"""o/pThe LCM of 54 and 24 is 216"""
#18.Python program to find HCF
"""def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 65 
num2 = 25
print("The H.C.F. is", compute_hcf(num1, num2))"""
"""o/p
The H.C.F. is 5"""
#5.quadratic equation:
"""a = int(input("Enter a:")) 
b = int(input("Enter b:")) 
c = int(input("Enter c:"))
d = (b**2) - (4*a*c)
x= (-b+(0.5**d))/(2*a)
x1=(-b-(0.5**d))/(2*a)
print(x,x1)"""
"""o/p:
Enter a:12
Enter b:35
Enter c:36
1.0911302026320472e+150 -1.0911302026320472e+150"""










