def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return  a/b

num1 = float(input("Enter first number:"))

op = input("select operator which you want to print:")

num2 = float(input("Enter second number"))

if op == '+':
    print(num1, '+', '=', add(num1, num2))
elif op == '-':
    print(num1, '-', '=', subtract(num1, num2))
elif op == '*':
    print(num1, '*', '=', multiply(num1, num2))
elif op == '/':
    print(num1, '/', '=', divide(num1, num2))
else:
    "invalid input"

# Create a function covid( ) & it should accept patient name, and body temperature, by default the body
# temperature should be 98 degree

def covid(patient_name,body_temperature):
    if body_temperature < str(0) :
        default=str(98)
        print("Patient Name is ",patient_name," Body Temperature is ",default)
    else:
        print("Patient Name is ",patient_name," Body Temperature is ",body_temperature)
covid("Rahul", "") 
covid("Rahul", "99")




