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









class Bank:
    def __init__(self, acholdername, acno, balance):
        self.acholdername = acholdername
        self.acno = acno
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def checkBalance(self):
        print(f"Available Balance: ₹{self.balance}")


obj = Bank("Janavi Gol", 123456, 50000)

print("🏦 Welcome to the Bank System")
print(f"Account Holder: {obj.acholdername}")
print(f"Account Number: {obj.acno}\n")

obj.checkBalance()
obj.deposit(10000)
obj.withdraw(20000)
obj.checkBalance()
obj.withdraw(50000) 
