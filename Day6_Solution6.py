# Write a Python script to merge two Python dictionaries

def Merge(Dict1, Dict2):
    return (Dict2.update(Dict1))

Dict1 = {'a':20, 'b':30, 'c':40}
Dict2 = {'d':50, 'e':60}

My_Dict = Merge(Dict1, Dict2)

print(Dict2)

# Write a Python program to remove a key from a dictionary

My_Dict = {'Abhishek':'Bihar', 'Aparna':'Odisha', 'Ankit':'Chennai', 'Raushan':'Delhi'}

print("Dictionary item :", My_Dict )

key = input("Enter the key that you want to delete: ")

if key in My_Dict:
    del My_Dict[key]

else:
    print("The given key is not in Dictionary")

print("\nUpdated Dictionary", My_Dict)

#  Write a Python program to map two lists into a dictionary

Student_name = ['Abhishek', 'Aparna', 'Ankit', 'Rahul']
Student_mark = [300, 250, 260, 270]

Student_data = dict(zip(Student_name,Student_mark))
print(Student_data)

# Write a Python program to find the length of a set

Set = {"Dhoni", "Jdeja", "Virat", "Rohit"}

print(len(Set))

# Write a Python program to remove the intersection of a 2nd set from the 1st set

Set1 = {2,4,6,8,12,16,20}
Set2 = {4,6,12,8,5,7}
print(Set1.intersection(Set2))