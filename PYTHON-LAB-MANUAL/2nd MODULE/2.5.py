# 2.5	Create a NumPy array of numbers from 1 to 10.

#    •	Perform sum, mean, median, and standard deviation.
#    •	Multiply the array by 2.
#    •	Extract elements from index 3 to 7.
#    •	Reverse the array using slicing.


import numpy as np

array = np.arange(1,11)

sum = np.sum(array)
print(f"Sum: {sum}")

mean = np.mean(array)
print(f"Mean: {mean}")

med = np.median(array)
print(f"Median: {med}")

stend = np.std(array)
print(f"Stend: {stend}")


multi = array * 2
print(f"Multiplication: {multi}")

indx = array[3:7]
print(f"Index: {indx}")

reverse = array[::-1]
print(f"Reverse: {reverse}")