'''
# Single Inheritance:

class parent:

    def func1(self):
        print("This is parent function")

class child(parent):
    def func2(self):
        print("this is child function")

ob = child()
ob.func1()
ob.func2()

# Multiple inheritance

class parent:
    def func(self):
        print("This is first example")

class parent2:
    def func2(self):
        print("this is second example")

class child(parent,parent2):
    def func3(self):
        print("This is third example")

ob = child()
ob.func()
ob.func2()
ob.func3()

class parent:
    def func(self):
        print("This is first example")

class child(parent):
    def func2(self):
        print("this is second example")

class child2(child):
    def func3(self):
        ("This is third example")

ob = child2()
ob.func()
ob.func2()
ob.func3()

# Hierarchical Inheritance

class parent:
    def func(self):
        print("This is example first")

class child(parent):
    def func2(self):
        print("This is second example")

class child2(parent):
    def func3(self):
        print("tThis is example three")

ob = child()
ob1 = child2()
ob.func()
ob.func2()

# Hybrid Inheritance

class Parent:
    def func1(self):
        print("this is example 1")


class Child(Parent):


    def func2(self):
        print("this is example 2")


class Child1(Parent):
    def func3(self):
        print(" this is example 3")


class Child3(Parent, Child1):
    def func4(self):
        print(" this is example 4")


ob = Child3()
ob.func1()

# super() function

class Parent:
     def func1(self):
         print("this is example 1")
class Child(Parent):
     def func2(self):
          Super().func1()
          print("this is example 2")

ob = Child()
ob.func2()
Method Overriding

class Parent:
    def func1(self):
        print("this is parent function")

class Child(Parent):
    def func1(self):
        print("this is child function")

ob = Child()
ob.func1()
'''


class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("personal detail")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

Abhishek = User('Abhishek', 21, 'male')
Abhishek.show_details()

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0


    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("The amount has been updated: RS ",self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount> self.balance:
            print("insufficient fund | Available balance is: RS",self.balance)
        else:
            print("The updated balance is: RS",self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance",self.balance)

Abhishek = Bank('Abhishek', 20, 'male')
Abhishek.deposit(1000)
Abhishek.withdraw(100)
Abhishek.withdraw(1100)
Abhishek.view_balance()

