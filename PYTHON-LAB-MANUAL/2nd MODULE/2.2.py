"""2.2	Tuple Operations

•	Create a tuple of 5 subject names.
•	Access the 2nd and last element.
•	Try to change the 3rd element and note the error."""


tuple = ("MATH","PHYSICS","CHEMISTRY","BIOLOGY","PYTHON PROGRAMMING")
print(tuple[1])
print(tuple[-1])

#  Try to change 3rd elements
tuple[2] = "JAVA"
print(tuple[2])

"""
Traceback (most recent call last):
  File "c:\Users\ritik\OneDrive\Desktop\PYTHON\PYTHON-LAB-MANUAL\2nd MODULE\2.2.py", line 13, in <module>
    tuple[2] = "JAVA"
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment

"""

#  Tuple are immutable