class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getdata(self):
        pass

class Develper(Employee):
    def __init__(self, name, age,id,salary):
        self.id=id
        self.salary=salary
        super().__init__(name, age)

    # def set_sale(self,id,salary):  
    #     self.id =id
    #     self.salary=salary

    def getdata(self):
        print("Devoper Details: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employrr ID: {self.id}")
        print(f"Salary: {self.salary}")
        

class Manager(Employee):
    def __init__(self, name, age,id,salary,department):
        self.id=id
        self.salary=salary
        self.deparement=department
        super().__init__(name, age)

    # def set_show(self,id,salary):  
    #     self.id =id
    #     self.salary=salary

    def getdata(self):
        print("Devoper Details: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employrr ID: {self.id}")
        print(f"Salary: {self.salary}")
    


man=[]  
dev=[]

print("--- Python OOP Project: Employee Management System --- \n")

while True:
    print("Choose an operation:")
    print("1.Creat an Devloper")
    print("2.Creat a Manager")
    print("3.Show Details")
    print("0.Exit \n")

    choice=int(input("Enter your choice: "))
    print()

    # if choice==1:
    #     name=input("Enter Name: ")
    #     age=int(input("Enter Age: "))
        
    #     eobj=Employee(name,age)
    #     emp.append(eobj)
    #     print()
    #     print(f"Employee created with name: {name} and age: {age}. \n ")
    #     print("--- Choose another operation --- \n ")


    if choice==1:
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        id=input("Enter Employee ID: ")
        salary=int(input("Enter Salary: ")) 
        dobj=Develper(name,age,id,salary)
        dev.append(dobj)
        print()
        print(f"Devloper created with name: {name}, age: {age}, ID: {id}, salary: {salary}. \n")
        print("--- Choose another operation ---\n")


    elif choice==2:
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        id=input("Enter Employee ID: ")
        salary=int(input("Enter Salary: "))
        dep=input("Enter Department: ")

        mobj=Manager(name,age,id,salary,dep)
        man.append(mobj)
        print()

        print(f"Manager created with name: {name}, age: {age}, ID: {id}, salary: {salary}, and department: {dep}\n ")
        print("--- Choose another operation ---\n")

    elif choice==3:
        print("Choose details to show: ")
        print("1.Devloper")
        print("2.Manager \n")

        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
           for obj in dev:
                obj.getdata()
        
        elif choice==2:
            for obj in man:
                obj.getdata()

        else:
            print("your choice is not valid.")

    elif choice==5:
        print("Exiting the system. All resources have been freed. \n")
        print("Goodbye!")
        break

    else:
        print("your choice is not valid.")
   


