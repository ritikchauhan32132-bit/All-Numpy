# big number
a = int(input("Enter 1 Number: "))
b = int(input("Enter 2 Number: "))
c = int(input("Enter 3 Number: "))

if a > b and a > c:
    print(f"This Is a Big Number: {a}")
    
elif b > a and b > c:
    print(f"This Is a Big Number: {b}")
    
elif c > b and c > a:
    print(f"This Is a Big Number: {c}")
    
else:
    print("All Numbers Are Same!")