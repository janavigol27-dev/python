class Employee:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.__id=id
        self.__salary=salary

    def getdata(self):
        return self.__id
    
    def getdata(self):
        return self.__salary
    
    def set_id(self,id):
        self.__id =id

    def set_salary(self, salary):
        self.__salary = salary

    def getdata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.__id}")
        print(f"Salary: {self.__salary}")

class Develper(Employee):
    def __init__(self, name, age, id, salary, programing_language ):
        self.programing_language=programing_language
        super().__init__(name, age,id,salary)

    def __del__(self):
        pass

    def parentcheck(self):
        issubclass(Develper,Employee)

    def getdata(self):
        print("Devoper Details: ")
        super().getdata()
        print(f"Programming Language: {self.programing_language}")

class Manager(Employee):
    def __init__(self, name, age,id,salary,department):
        self.department=department
        super().__init__(name, age, id, salary)

    def __del__(self):
        pass

    def parentcheck(self):
        issubclass(Manager,Employee)

    def getdata(self):
        print("Manager Details: ")
        super().getdata()
        print(f"Department: {self.department}")

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
    
    if choice==1:
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        id=input("Enter Employee ID: ")
        salary=int(input("Enter Salary: ")) 
        pro=input("Enter your programing language: ")

        dobj=Develper(name,age,id,salary,pro)
        dev.append(dobj)
        print(f"\nDevloper created with name: {name}, age: {age}, ID: {id}, salary: {salary}. \n")
        print("--- Choose another operation ---\n")

    elif choice==2:
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        id=input("Enter Employee ID: ")
        salary=int(input("Enter Salary: "))
        dep=input("Enter Department: ")

        mobj=Manager(name,age,id,salary,dep)
        man.append(mobj)
        print(f"\nManager created with name: {name}, age: {age}, ID: {id}, salary: {salary}, and department: {dep}\n ")
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
                print()

        elif choice==2:
            for obj in man:
                obj.getdata()
                print()
        else:
            print("Invalid choice.\n")
            break

    elif choice==0:
        print("Exiting the system. All resources have been freed. \n")
        print("Goodbye!")
        break

    else:
        print("your choice is not valid.\n")
        break


