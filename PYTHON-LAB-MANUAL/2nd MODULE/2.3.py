"""
2.3	Set Operations

•	Create two sets of marks obtained in two exams.
•	Find union, intersection, and difference.
•	Add a new mark to the first set.


"""

a = {85, 90, 78, 92, 88}
b = {80, 90, 75, 92, 86}

print("Set A:", a)
print("Set B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

a.add(95)
print("After adding 95:", a)