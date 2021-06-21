# 1.Write a program to loop through a list of numbers and add +2 to every value to elements in list

list = [2,3,5,6,9,6,10]

New_list = [x + 2 for x in list]
print(New_list)

# 2.Write a program to get the below pattern

rows = int(input("Enter the number of rows: "))
for i in range(0, rows + 1):
    # inner loop for decrement in i values
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()


# Python Program to Print the Fibonacci sequence

nterms = int(input("How many terms you want? "))
# first two terms
n1 = 0
n2 = 1
count = 2
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   print(n1,",",n2,end=', ')
   while count < nterms:
       nth = n1 + n2
       print(nth,end=' , ')
       # update values
       n1 = n2
       n2 = nth
       count += 1

# •	Explain Armstrong number and write a code with a function

from math import *
number = int(input("Enter the number : "))
result = 0
n = 0
temp = number;
while (temp != 0):
    temp =int(temp / 10)
    n = n + 1

#Checking if the number is armstrong
temp = number
while (temp != 0):
    remainder = temp % 10
    result = result + pow(remainder, n)
    temp = int(temp/10)
if(result == number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Write a program to print the multiplication table of 9

num = int(input(" Enter the number : "))
# using for loop to iterate multiplication 10 times
print("Multiplication Table of : ")
for i in range(1,11):
   print(num,'x',i,'=',num*i)

# •	Check if a program is negative or positive

num = int(input("Enter a number:"))

if num > 0:
    print("Number us positive")

else:
    print("Number is negative")

# Write a program to convert the number of days to ages

days = int(input("Enter number of days:"))

years = days/365

print(years)


# solve trigonometry problem using math function WAP to solve using math function

import math
x = int(input("Enter value"))
print(math.sin(x),"sin")
print(math.cos(x),"cos")
print(math.tan(x),"tan")


#creat a calculator only on a code level by using if condition .
a=int(input("num1 "))
b=int(input("num2 "))
c=input("Enter operator")
if c == '+':
    print("Addition of two numbers",a+b)
elif c=='-':
    print("Subtraction of two numbers",a-b)
elif c=='*':
    print("Multiplication of two numbers",a*b)
elif c=='/':
    if a==0:
        print("Numerator cannot be zero")
    elif b==0:
        print("Zero division error")
    elif a==0 and b==0:
        print("Zero")
    else:
        print("Division of two numbes",a/b)
else:
    print("not found")

