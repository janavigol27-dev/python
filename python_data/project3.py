students=[]
print("Welcome to the Student Data Organizer! \n")

while True:
    print("Select an option : ")
    print("1.Add Student")
    print("2.Display All Student")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display Subject Offered")
    print("6.Exit \n")

    choice=int(input("Enter your choice : "))
    print()
    if choice==1:
        print("Enter Student details : ")
        listt={
            "id":int(input("Student ID : ")),
            "name":input("Name : "),
            "age":int(input("Age : ")),
            "grade":int(input("Grade : ")),
            "bod":input("Date of Birth (YYYY-MM-DD) : "),
            "subject":input("/Subjects (comma-seprated) :  ")
        }
        students.append(listt)
        print("\n Student added successfully!")
    
    elif choice==2:
        print("--- Display All Students ---")
        for i in students:
            print(f"Student ID:{i["id"]} | Name:{i["name"]} | Age:{i["age"]} | Grade:{i["grade"]} | subjects:{i["subject"]}  \n")
    
    elif choice==3:
        id=int(input("Enter your id : "))
         
        for i in students:
            if  i["id"]==id:
                i["name"]=input("Updated Name :"),
                i["age"]=int(input("Updated Age :")),
                i["grade"]=input("Updated Grade :"),
                i["bod"]=input("Updated Date of Birth (YYYY-MM-DD) : "),
                i["subject"]=input("Updated Subjects (ccomma-seprated) :")
                print("\n Student Updated Successfully ! \n")

    elif choice==4:
        id=int(input("Enter your id :"))

        for i in students:
            if i["id"]==id:
                students.remove(i)
                print("\n Student Removed Successfully ! \n ")

    elif choice==5:
        sub=[]
        id=int(input("Enter your id :"))

        for i in students:
            if i["id"]==id:
                if i["subject"]:
                    sub.append(i["subject"])
                    print(f"Display Subject Offered : {sub} \n")

    elif choice==6:
        print("\n Exit Our List.")
        break

    else:
        print("Your choice is not valid !")
        break

                

    
