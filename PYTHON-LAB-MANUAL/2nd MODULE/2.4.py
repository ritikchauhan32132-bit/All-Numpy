""" 
2.4	Dictionary Operations

•	Create a dictionary with 5 student names as keys and their marks as values.
•	Update marks for one student.
•	Add a new student with marks.
•	Remove one student from the dictionary.
•	Display all keys, values, and items.


"""
marks = 0
student = {
    "Ritik" : 87,
    "Vishal": 97,
    "Rohan":83,
    "Shubhangi":99,
    "Raushan" : 81
}

student["Ritik"] = 98
# print(student.values())

student["Munna"] = 91

# print(student)
for i in student.items():
    print(i)