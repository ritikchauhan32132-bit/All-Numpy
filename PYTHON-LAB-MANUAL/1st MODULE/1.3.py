# factorial
fact = 1
n = int(input("Enter a Number: "))
if n > 0:
    for i in range(1, n+1):
        fact = fact * i
        
    print(fact)
else:
    print("Please Enter The Vailed Number!")