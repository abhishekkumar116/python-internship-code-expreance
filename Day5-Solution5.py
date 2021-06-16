# solution for first question


l = eval(input('Enter list:'))
print(l)
l.append(eval(input('Enter a value to add in the list:')))
print('After adding the list is:', l)
l.remove(eval(input('Enter a value to remove from the list:')))
print('After removing the list is:', l)
print('The largest number is:', max(l))
print('The smallest number is:', min(l))

# Solution of second problem

t = eval(input('Enter tuple element:'))
print('The reverse of the tuple:', t[::-1])

# solution of third problem

t = eval(input('Enter tuple'))
print(type(t))
l = []
print(list(t))
print(type(l))




