# pelindrom

def pelindrom():
    check = input("Enter A String: ")
    val = check[::-1]
    
    if check == val:
        print("This Is a Pelindrom!")
    else:
        print("This Is a Not Pelindrom!")
        
pelindrom()