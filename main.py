# #  <===  OBJECT ORINTED PROGRAMMING  ==>

# class Student:
#     name = "Ritik Kumar"
#     age = 19
#     classe = "BCA"
    
# s1 = Student()
# print(s1.name)
# print(s1.age)
# print(s1.classe)


# class Mobile:
#     brand = "Samsung"
#     model = "S24"
#     price = 50000
    
# m1 = Mobile()
# print(m1.brand)
# print(m1.model)
# print(m1.price)

# class Employee:
#     name = "unknown"
#     salary = 15000
    
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()

# e1.name = "Ritik"
# e2.name = "Rahul"
# e3.name = "Aman"

# e1.salary = 20000
# e2.salary = 25000
# e3.salary = 30000

# print(e1.name)
# print(e2.name)
# print(e3.name)

# print(e1.salary)
# print(e2.salary)
# print(e3.salary)


# class Const:
#     def __init__(self):
#         print("Constructor Created...")

# c1 = Const()
# c1 = Const()

# class Student:
#     def __init__( self , name , age , course ):
#         self.name = name
#         self.age = age
#         self.course = course
        
# s1 = Student( "Ritik" , 20 , "BCA" )
# s2 = Student( "Rahul" , 21 , "BBA" )
# s3 = Student( "Aman" , 19 , "BCA")


# print("Name: ",s1.name)
# print("Age: ",s1.age)
# print("Course: ",s1.course)
# print()

# print("Name: ",s2.name)
# print("Age: ",s2.age)
# print("Course: ",s2.course)
# print()

# print("Name: ",s3.name)
# print("Age: ",s3.age)
# print("Course: ",s3.course)
# print()


# class Student:

#     def __init__(self, name):
#         self.name = name

#     def change_name(self, new_name):
#         self.name = new_name


# s1 = Student("Ritik")
# s2 = Student("Rahul")

# s1.change_name("Aman")

# print(s1.name)
# print(s2.name)

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
    
#     def show_balance(self):
#         print(f"Name: {self.name}")
#         print(f"{self.name} Balance: {self.balance}")
    
#     def deposite(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print("Ammount Deposit Successfully!")
#         else:
#             print("Invailed Ammount!")
        
        
# c1 = BankAccount("Ritik",5000)
# c2 = BankAccount("Rahul",10000)

# c1.deposite(2000)

# c1.show_balance()
# c2.show_balance()



# class Student:

#     college = "MATS University"

#     def __init__(self, name):
#         self.name = name


# s1 = Student("Ritik")
# s2 = Student("Rahul")

# s1.college = "IIT Bombay"

# print(s1.college)
# print(s2.college)
# print(Student.college)



# class Student:
#     college = "NIT ROORKEY"
    
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Name: {self.course}")
#         print(f"College: {self.college}")
      
# s1 =Student( "Ritik" , 20 , "BCA" )
# s2 =Student( "Rahul" , 21 , "BBA" )
# s3 =Student( "Aman" , 19 , "BCA" )

# s1.show_details()
# s2.show_details()
# s3.show_details()

# class Employee:
#     company = "Google"
    
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Company: {self.company}")
#         print()
        
# e1 = Employee("Ritik",30000)
# e2 = Employee("Rahul",40000)
# e3 = Employee("Aman",50000)

# e1.show_details()
# e2.show_details()
# e3.show_details()


# Employee.company = "Microsoft"

# e1.show_details()
# e2.show_details()
# e3.show_details()


# class Calculator:
    
#     def __init__(self,number1,number2):
#         self.num1 = number1
#         self.num2 = number2
        
#     def add(self):
#         print(f"Addition: {self.num1 + self.num2}")
        
#     def subtract(self):
#         print(f"Subtraction: {self.num1 - self.num2}")
        
#     def multiply(self):
#         print(f"Multiplication: {self.num1 * self.num2}")
        
#     def divide(self):
#         if self.num2 != 0:
#             print(f"Division: {self.num1 / self.num2}")
#         else:
#             print("Invailed Number!")
        
# c1 = Calculator(20,10)
# c1.add()
# c1.subtract()
# c1.multiply()
# c1.divide()



# class Employee:

#     company = "Google"

#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print(self.name)

#     @classmethod
#     def change_company(cls, company):
#         cls.company = company

#     @staticmethod
#     def welcome():
#         print("Welcome to Employee Management System!")


# e1 = Employee("Ritik")

# e1.show_name()

# Employee.change_company("Microsoft")

# Employee.welcome()

# print(Employee.company)


# class Student:
#     college = "MATS University"
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Marks: {self.marks}")
#         print(f"College: {self.college}")
        
        
        
#     @classmethod
#     def change_college(cls,new_clg_name):
#         cls.college = new_clg_name
        
#     @staticmethod
#     def check_pass(marks):
#         if  marks >= 33:
#             print("PASS")
#             print()
#         else:
#             print("FAIL")
#             print()
    
# s1 = Student("Ritik", 85)
# s2 = Student("Rahul", 25)
# Student.check_pass(85)
# Student.check_pass(25)

# print("Before College Change !\n")

# s1.show_details()
# s2.show_details()


# Student.change_college("Microsoft University!")
# s1.show_details()
# s2.show_details()

# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self._account_type = "Savings"
#         self.__balance = balance

#     def show_balance(self):
#         print("Name:", self.name)
#         print("Balance:", self.__balance)


# account1 = BankAccount("Ritik", 10000)

# account1.show_balance()

# print(account1.name)
# print(account1._account_type)


# class Student:
#     def __init__(self,name,course,marks):
#         self.name = name
#         self._course = course
#         self.__marks = marks
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Course: {self._course}")
#         print(f"Marks: {self.__marks}")
        
# s1 = Student("Ritik","Data Scince",85)
# s1.show_details()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks

#     # Getter
#     def get_marks(self):
#         return self.__marks

#     # Setter
#     def set_marks(self, new_marks):
#         if 0 <= new_marks <= 100:
#             self.__marks = new_marks
#             print("Marks updated successfully!")
#         else:
#             print("Invalid marks!")


# s1 = Student("Ritik", 85)

# print("Old Marks:", s1.get_marks())

# s1.set_marks(95)

# print("New Marks:", s1.get_marks())

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.__marks = marks
        
#     @property
#     def marks1(self):
#         return self.__marks
    
#     @marks1.setter
#     def marks1(self,new_marks):
#         if 0 <= new_marks <= 100:
#             self.__marks = new_marks
#             print("Marks Successfully Updated!")
#         else:
#             print("Invalid Marks!")
            
# s1 = Student("Ritik",85)
# print(f"Name: {s1.name} \nOld Marks: {s1.marks1}")
# s1.marks1 = 95
# print(f"New Marks: {s1.marks1}")
# s1.marks1 = 150


# class Vehicle:
    
#     def start(self):
#         print("Vehicle Started!")
        
#     def stop(self):
#         print("Vehicle Stopped!")
    
# class Car(Vehicle):
    
#     def drive(self):
#         print("Car Is Driving!")
        
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike Is Riding!")
        
# c1 = Car()
# c1.start()
# c1.stop()
# c1.drive()

# print()

# b1 = Bike()
# b1.start()
# b1.stop()
# b1.ride()

class Employee:
    def __init__(self,name):
        self.name = name
        
    def show_role(self):
        print("Employee works in a company!")
        
class Developer(Employee):
    def __init__(self,name,language):
        self.name = name
        self.language = language
        super().__init__(name)
        
    def show_role(self):
        print("Developer writes code!")
        
    def show_language(self):
        print(f"Language: {self.language}")
        
d1 = Developer("Ritik", "Python")
print(f"Name:{d1.name}")
d1.show_role()
d1.show_language()