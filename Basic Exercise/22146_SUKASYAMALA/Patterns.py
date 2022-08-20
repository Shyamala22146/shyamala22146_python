#1. Write a program to print the following Patterns
"""  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5"""
"""for row in range(1,6):
    for col in range(1,6):
        print(col,end=" ")
    print()"""
"""1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 """
#===============================================================================
#2.2.Write a program to print the following Pattern
"""5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1"""
"""for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(col,end=" ")
    print()"""
"""5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1"""
#===============================================================================
#3Write a program to print the following Pattern
"""5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1"""
"""for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(row, end=" ")
    print()"""
"""5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1"""
#====================================================================================
#4.4.Write a program to print the following Pattern
"""1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5"""
"""for row in range(1,6):
    for col in range(1,row+1):
        print(col, end=" ")
    print()"""
"""o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5"""
#=====================================================================================
#5.Write a program to print the following Pattern
""" 1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5"""
"""for row in range(1,6):
    for col in range(1,row+1):
        print(row, end=" ")
    print()"""
"""o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """
#===============================================================================    
#6.Write a program to print the following Pattern
"""1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15"""
"""n=1
stop = 2  
rows = 5  
  
for i in range(rows):  
    for j in range(1, stop):  
        print(n, end=' ')  
        n += 1  
    print("")  
    stop += 1"""
"""o/p
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15"""
#======================================================================================
#7.Write a program to print the following Pattern
"""5
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1"""
"""k = 5
for row in range(1,5+1):
    val = (str(k)+ " ")* row
    print(val)
    k -= 1"""
"""o/p:
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 """
#===========================================================================================
  #8..Write a program to print the following Pattern
""" 1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 """

#9.Write a program to print the following Pattern
""" A 
  B C
  D E F
  G H I J
  K L M N O"""
"""ascivalue=65
for i in range(0,5):
    for j in range(0,i+1):
        alp=chr(ascivalue)
        print(alp, end=' ')
        ascivalue+=1
    print()"""
"""o/p:
A 
B C 
D E F 
G H I J 
K L M N O"""
#===============================================================================
#11.Write a program to print the following Pattern
""" * 
* * 
* * * 
* * * * 
* * * * * """

"""for row in range(6):
    for col in range(row):
        print("*", end=" ")
    print()"""
"""O/p
* 
* * 
* * * 
* * * * 
* * * * *"""
#======================================================================================
#12.Write a program to print the following Pattern
"""* * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * """
"""n = 5
for row in range(1,n+1):
    for col in range(1,n+1):
        if(col == 1 or col == n) or (row == 1 or row == n):
            print('*',end="")
        else:
            print(" ",end="")
    print()"""
"""*****
*   *
*   *
*   *
*****"""
#==============================================================================================
#13.Write a program to print the following Pattern
"""num = 1
for row in range(4,0,-1):
    for col in range(row,0,-1):
        print(' ',end=' ')
    print(' *'*num)
    num+=2"""

"""O/p
        *
       * * *
     * * * * *
   * * * * * * *"""
#==============================================================================================
#14.Display Multiplication Table in given range using Nested for loops
"""n=int(input("enter a number:"))
for i in range(3):
    for j in range(1,11):
        print (i,"*", j,"=", i*j)
    print()"""
"""enter a number:3
0 * 1 = 0
0 * 2 = 0
0 * 3 = 0
0 * 4 = 0
0 * 5 = 0
0 * 6 = 0
0 * 7 = 0
0 * 8 = 0
0 * 9 = 0
0 * 10 = 0

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20"""
#======================================================================
#15.Display Prime Numbers in the given range using nested for loops
"""for i in range(2,100):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i,end=' ')"""
"""o/p:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 """




