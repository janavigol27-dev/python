import os

class journalmanager:
    def __init__(self):
        self.filename="journal.txt"

    def add(self):
        added=input("Enter your journal entry : ")
        try:
            with open(self.filename,"a") as file:
                file.write(added + "\n")
                print()
                print("Entry added successfully !\n")
        except Exception:
            print()
            print("first add some entries.\n ")

    def show(self):
        try:
            with open (self.filename,"r") as file:
                print("Your journal entries : ")
                print("---------------------------")
                entries=file.readlines()
                if entries:
                    for i in entries:
                        print(i)
                else:
                    print("\n No journal entries found .Start by adding a new entry ! ")
        except Exception:
            print("\n Error: The journal file dose not exist. Please add a new entry first.")

    def search(self):        
        keyword = input("Enter a keyword or date to search: ")
        print()
        try:
            with open(self.filename, "r") as file:
                entries = file.readlines()
                match = [entry.strip() for entry in entries if keyword.lower() in entry.lower()]
                if match:
                    print()
                    print("Matching Entries:")
                    print("---------------------")
                    if entries:
                        for i in match:
                            print(i)
                else:
                    print()
                    print(f"No entries were found for the keyword :{keyword} .\n")
        except Exception:
            print()
            print("No match journal entries found.\n ")

    def delete(self):
        empty=input("Are you sure you want to delete all enteries (yes/no):  ")
        try:
            if empty=="yes":
                self.filename=open("journal.txt","w")
                self.filename.close()
                print()
                print("All journal entries have been deleted.\n")
            else:
                print()
                print("Not deleted\n")
        except Exception:
            print()
            print("No journal entries to delete.\n ")


print("Welcome to Personal Journal Manager !")

while True:
    print("Please Select an option : \n")

    print("1. Add New Entry")
    print("2.View All Entries")
    print("3.Search for an Entry")
    print("4.Delete All Entries")
    print("5.Exit \n")

    choice=int(input("User Input : "))
    print()

    if choice==1:
        obj=journalmanager()
        obj.add()
    elif choice==2:
        obj=journalmanager()
        obj.show()
    elif choice==3:
        obj=journalmanager()
        obj.search()
    elif choice==4:
        obj=journalmanager()
        obj.delete()
        break
    elif choice==5:
        print("Thank you for using personal journal manager. Goodbye !\n")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.!!\n")
        break

        