import time
# # Question 1: Ek list banao jisme 5 numbers hon aur third element print karo.

# list = [1,2,3,4,5]
# print(list[2])

# # Question 2: List [10, 20, 30, 40] mein 20 ko 200 se replace karo.

# list = [10, 20, 30, 40]
# list[1] = 200
# print(list[1])

# # Question 3: List [1, 2, 3, 4] ke end mein 5 add karo.

# list = [1, 2, 3, 4]
# list.append(5)
# print(list)

# # Question 4: List [10, 20, 30, 40] se 30 remove karo.

# list = [10, 20, 30, 40]
# list.remove(30) # ye value ko khoj ke hata dega
# list.remove(list[2]) # ye 2nd index se value remove kar dega
# print(list)

# # Question 5: List [5, 10, 15, 20] ke saare elements for loop se print karo.

# list = [5, 10, 15, 20]
# for i in list:
#     print(i)

# start = time.time()
# numbers = []
# for i in range(10):
#     numbers.append(i)

# print(numbers)
   
# print("Numbers Added!")

# print(start-time.time())

# outer = ["bhindi"]
# inner = ["Aalu"]

# for i in range(3):
#     for j in range(3):
#         print(inner)
#     print(outer)


# # 3. Traversal

list = [1,2,3,4,5,6,7,8,8,8,8]
# for i in list:
#     print(i)
    
#  Updating

list[2] = 9
# print(list)

list.insert(2,7)
# print(list)

# Deletation

list.pop(8)
# print(list)
# while 8 in list:
#     list.pop(8)
    
# print(list)

# Searching

# target = 8
# for i in range(len(list)):
#     if list[i] == target:
#         print(f"Traget Found At: {i}")
#         break
#     else:
#         print("Target Is Not Found!")


# # Problem 1: Find the largest element
# arr = [10, 50, 20, 90, 40]
# # print(max(arr))

# largest = arr[0]
# for num in arr:
#     if num > largest:
#         largest = num
# print(largest)

# # Problem 2: Find the smallest element

# arr = [10, 50, 20, 90, 40]
# small = arr[0]
# for num in arr:
#     if num < small:
#         small = num
# print(small)


0


# # Problem 3: Calculate the sum of array

# arr = [10, 20, 30, 40]
# total = 0
# for i in arr:
#     total += i

# print(f"Sum: {total}")


# # Problem 4: Count even and odd numbers

# arr = [10, 15, 20, 25, 30]

# for i in arr:
#     if i % 2 == 0:
#         print(f"Even: {i}")
#     else:
#         print(f"Odd: {i}")

# Problem 5: Reverse an array without using reverse()

# arr = [10, 20, 30, 40, 50]
# rev = []
# # print(arr[::-1])
# for i in arr:
#     rev.insert(0,i)
    
# print(rev)

# largest number

# a = [10, 20, 30, 40, 50 , 90 , 18]

# largest = a[0]

# for num in a:
#     if num > largest:
#         largest = num
        
# print(largest)

