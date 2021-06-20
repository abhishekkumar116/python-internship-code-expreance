# 1. Write a Python script to merge two Python dictionaries

def Merge(dict1,dict2):
    return dict1,dict2

dict1 = {'Abhishek':'Bihar', 'Ankit':'Delhi', 'Rahul':'Chennai'}
dict2 = {'Rohit':'Mumbai', 'Raushan':'Kolkata' }
dict3 = Merge(dict1,dict2)
print(dict3)

# 2. Write a program to sort the value from descending to ascending in list and
# convert it in to a set.

list = [50, 30, 25, 20, 18, 10]
list.sort()
print(list)

s = set(list)
print(s)

# 3. Write a Python program to list number of items in a dictionary key and sort the
# list with the help of a function & without the function.

dic1={'Divesh':[12,13,31,16],'Renuka':[12,77,54,43],'Shriram':[34,87,28,98],'Anuj':[33,66,55,44]}
result={k:sorted(dic1[k]) for k in sorted(dic1)}
print(result)

# using function

def function2(dic1):
    res=dict()
    min1=dic1[key]
    for key in sorted(dic1):
        if dic1[key]<min1:
            min1=dic1[key]
            res[key]=min1
    return res


# 4.Write a Python program to get a string from a given string (user input) and
# change the first occurrence of the word to a user specified input

string = input("Enter a string:")
print(string)

user_input = input("Enter specified input which you want to replace:")
print(string[ :0] + user_input + string[1: ])


# 5.Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to capital letter.

string = input("Enter a string:")

print(string.capitalize())

# 6.Write a Python program to find the repeated items of a list

list = [1,2,4,5,6,8,5,4,2,1,8,9]
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

# 7.Write a Python program to check the sum of three elements and divided by a
# value which is given as an input by the user

a = int(input("Enter 1st value:"))
b = int(input("Enter 2nd value:"))
c = int(input("Enter 3rd value:"))

sum = a+b+c
print(sum)
e = int(input("Enter a value to divide:"))

x = sum/e
print(x)

# 8.Write a Python program to find the Mean,median,mode among three given
# numbers

given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)


# 9.Write a Python program to swap cases of a given string

string = "Best Enlist"

print(string.swapcase())

string = "Internship"
print(string.swapcase())

# 10.Write a program to convert an integer to binary & octa decimal

num = int(input("Enter an integer value:"))
Binary_form = bin(num)
print(Binary_form)
Octal_decimal = oct(num)
print(Octal_decimal)