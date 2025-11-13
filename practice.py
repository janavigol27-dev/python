# class person:
#     def greet(self):
#         print("Hello")

#     def once(self):
#         print("hii")

# obj=person()
# obj1=person()

# obj.greet()
# obj1.once()






# class car:
#     brand:None
#     model:None
#     year:None

# car1=car()

# car1.brand="Honda"
# car1.model="Civic"
# car1.year=2023

# print(car1.brand,car1.model,car1.year)


# class book:
#     auther:None
#     page:None
#     year:None

# book1=book()

# book1.auther="kalidas"
# book1.page=200
# book1.year=2023

# print(book1.auther,book1.page,book1.year)

# class bike:
#     brand:None
#     model:None
#     year:None

# bike1=bike()

# bike1.brand="shine"
# bike1.model="125 obd2b"
# bike1.year=2025

# print(bike1.brand,bike1.model,bike1.year)







# class Person:
#     def __init__(self):
#         print("Hello")
#         self.name="janavi"
#         self.age=12

#     def greet (self):
#         print("Hello from greet")

# obj=Person()
# obj.greet() 
# print(obj.name) 
# print(obj.age) 


# class chocklate:
#     def __init__(self):
#         print("Hello welcome to our choco world!")
#         self.name="dairy milk silk"
#         self.sweetnace=50

#     def greet (self):
#         print("Hello from chocklate")

# obj=chocklate()
# obj.greet() 
# print(obj.name) 
# print(obj.sweetnace) 


# class beauty:
#     def __init__(self):
#         print("Hello beauty world !")
#         self.brand="mar's"
#         self.year=2020

#     def greet (self):
#         print("Hello cutie !")

# obj=beauty()
# obj.greet() 
# print(obj.brand) 
# print(obj.year) 








# class Person:
#     def __init__(self):
#         print("Hello")
#         self.name=None
#         self.age=None

#     def greet (self):
#         print("Hello from greet")

# obj=Person()
# obj.greet() 
# obj.age=22
# obj.name="janavi"
# print(obj.name) 
# print(obj.age) 



# class book:
#     def __init__(self):
#         print("Hello")
#         self.name=None
#         self.year=None

#     def greet (self):
#         print("Hello from book world!")

# obj=book()
# obj.greet() 
# obj.year=2022
# obj.name="titenick"
# print(obj.name) 
# print(obj.year) 



# class colony:
#     def __init__(self):
#         print("Hello new naighberhood")
#         self.name=None
#         self.year=None

#     def greet (self):
#         print("Hello from our partner!")

# obj=colony()
# obj.greet() 
# obj.year=2022
# obj.name="sonali"
# print(obj.name) 
# print(obj.year) 






# class Person:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#     def greet(self):
#         print(f"hello from {self.name} and his city is {self.city} . ")

# obj=Person("janavi",22,"rajkot")
# obj1=Person("jeni",12,"amreli")

# obj.greet()
# obj1.greet()



# class Person:
#     def __init__(self,name,age,city,gender):
#         self.name=name
#         self.age=age
#         self.city=city
#         self.gender=gender

#     def greet(self):
#         print(f"hello from {self.name} and his city is {self.city} . ")

# obj=Person("janavi",22,"rajkot","women")
# obj1=Person("jenil",12,"amreli","men")

# obj.greet()
# obj1.greet()





# class apprtment:
#     def __init__(self,name,year,city,location):
#         self.name=name
#         self.year=year
#         self.city=city
#         self.location=location

#     def greet(self):
#         print(f"hello from {self.name} and his city is {self.city} . ")

# obj=apprtment("nandan",2023,"rajkot","matuki hotel")
# obj1=apprtment("krishn bhoomi"2022,"amreli","mavdi")

# obj.greet()
# obj1.greet()









# class Bank:
#     def __init__(self, acholdername, acno, balance):
#         self.acholdername = acholdername
#         self.acno = acno
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"₹{amount} deposited successfully.")
#         else:
#             print("Invalid deposit amount.")
            
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         elif amount <= 0:
#             print("Invalid withdrawal amount.")
#         else:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn successfully.")

#     def checkBalance(self):
#         print(f"Available Balance: ₹{self.balance}")


# obj = Bank("Janavi Gol", 123456, 50000)

# print("🏦 Welcome to the Bank System")
# print(f"Account Holder: {obj.acholdername}")
# print(f"Account Number: {obj.acno}\n")

# obj.checkBalance()
# obj.deposit(10000)
# obj.withdraw(20000)
# obj.checkBalance()
# obj.withdraw(50000) 












# class Employee:
#     def __init__(self, name, age, emp_id, salary):
#         self.name = name
#         self.age = age
#         self.__id = emp_id
#         self.__salary = salary

#     # Getter methods to access private data
#     def get_id(self):
#         return self.__id

#     def get_salary(self):
#         return self.__salary

#     # Setter methods (if salary/id need to be updated)
#     def set_id(self, emp_id):
#         self.__id = emp_id

#     def set_salary(self, salary):
#         self.__salary = salary

#     def getdata(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Employee ID: {self.__id}")
#         print(f"Salary: {self.__salary}")


# class Develper(Employee):
#     def __init__(self, name, age, emp_id, salary, programming_language):
#         super().__init__(name, age, emp_id, salary)
#         self.programming_language = programming_language

#     def __del__(self):
#         pass

#     def parentcheck(self):
#         print("Is Developer subclass of Employee?", issubclass(Develper, Employee))

#     def getdata(self):
#         print("\nDeveloper Details:")
#         super().getdata()
#         print(f"Programming Language: {self.programming_language}")


# class Manager(Employee):
#     def __init__(self, name, age, emp_id, salary, department):
#         super().__init__(name, age, emp_id, salary)
#         self.department = department

#     def __del__(self):
#         pass

#     def parentcheck(self):
#         print("Is Manager subclass of Employee?", issubclass(Manager, Employee))

#     def getdata(self):
#         print("\nManager Details:")
#         super().getdata()
#         print(f"Department: {self.department}")


# # Main Program
# man = []
# dev = []

# print("--- Python OOP Project: Employee Management System --- \n")

# while True:
#     print("Choose an operation:")
#     print("1. Create a Developer")
#     print("2. Create a Manager")
#     print("3. Show Details")
#     print("0. Exit \n")

#     choice = int(input("Enter your choice: "))
#     print()

#     if choice == 1:
#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         emp_id = input("Enter Employee ID: ")
#         salary = int(input("Enter Salary: "))
#         pro = input("Enter your Programming Language: ")

#         dobj = Develper(name, age, emp_id, salary, pro)
#         dev.append(dobj)
#         print(f"\nDeveloper created: {name}, Age: {age}, ID: {emp_id}, Salary: {salary}, Language: {pro}\n")

#     elif choice == 2:
#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         emp_id = input("Enter Employee ID: ")
#         salary = int(input("Enter Salary: "))
#         dep = input("Enter Department: ")

#         mobj = Manager(name, age, emp_id, salary, dep)
#         man.append(mobj)
#         print(f"\nManager created: {name}, Age: {age}, ID: {emp_id}, Salary: {salary}, Department: {dep}\n")

#     elif choice == 3:
#         print("Choose details to show:")
#         print("1. Developer")
#         print("2. Manager\n")

#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             for obj in dev:
#                 obj.getdata()
#         elif ch == 2:
#             for obj in man:
#                 obj.getdata()
#         else:
#             print("Invalid choice.\n")

#     elif choice == 0:
#         print("\nExiting the system. Goodbye!")
#         break

#     else:
#         print("Invalid choice.\n")



main=[]

print("Welcome to our planner !\n")

while True:
    print("1.creat file")
    print("2.write file")
    print("3.append file")
    print("4.read file")
    print("0.Exit \n ")

    choice=int(input("Enter your choice : "))

    if choice==1:
        print()
        cre=input("your file name: ")
        file=open(cre,"w")
        file.write("")
        file.close()

        main.append(cre)
        print()
        print("your file is created ! \n")

    elif choice==2:
        print()
        con=input("your content print in this file : ")
        file=open(cre,"w")
        file.write(con)
        file.close()

        main.append(con)
        print()
        print("your content is successfully printed in this file ! \n")

    elif choice==3:
        print()
        app=input("your updeted content printed in this file : ")
        file=open(cre,"a")
        file.write(app)
        file.close()

        main.append(app)

        print("your content updeted successfully !\n")

    elif choice==4:
        print()
        print("your content : \n")

        for i in main:
            print(i)
        print()

    elif choice==0:
        print()
        print("Exit to our planner !\n")
        break

    else:
        print()
        print("your choice is not valid !\n")
        break
