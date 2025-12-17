import os
import datetime
import math
import random
import uuid
import time

while True:

    print("="*25 + "\n")
    print("Welcome to Multi-Utility Toolkit \n")
    print("="*25 + "\n")

    print("Choose an option : \n")
    print("1.Datetime and Time Operations")
    print("2.Mathematicale Operations")
    print("3.Random Data Genration")
    print("4.Genrate unique Identifires (UUID)")
    print("5.File Operations (Custome Module)")
    print("6.Explore Module Attribute")
    print("7.Exit \n")
    print("="*25 + "\n")

    choice=int(input("Enter your choice : "))
    print()

    if choice==1:
        while True:
            print("Datetime and Time Operations : \n")
            print("1.Display current date and time")
            print("2.Calculate difference between two dates/times")
            print("3.Formate date into custom format")
            print("4.Countdown Timer")
            print("0.Back to Main Menu \n")
 
            choice=int(input("Enter your choice : "))
            print()

            if choice==1:
                now=datetime.datetime.now()
                print(f"Current Date and Time :{now} \n")
                
            elif choice==2:
                one=input("Enter the first date (YYYY-MM-DD) : ")
                two=input("Enter the second date (YYYY-MM-DD) : ")
                print()
                one=datetime.datetime.strptime(one,"%Y-%m-%d")
                two=datetime.datetime.strptime(two,"%Y-%m-%d")
                difference=abs((two-one).days)
                print(f"Difference :{difference} days \n")
                
            elif choice==3:
                now=datetime.datetime.now()
                format=now.strftime("%d-%m-%Y %H:%M:%S")
                print(f"Formatted Date and time: {format}")
                print()
               
            elif choice==4:
                print("Countdown Timer :\n ")
                hours=int(input("Enter hours : "))
                minute=int(input("Enter minutes : "))
                second=int(input("Enter second : "))
                total=hours*3600 + minute*60 + second

                print(f"Countdown Timer :{total} second \n")

            elif choice==0:
                print("Back to Main Menu ! ")
                break

            else:
                print("Your choice is not valid !")

    elif choice==2:
            while True:
                print("Mathematical Operations : \n")
                print("1.Calculate Factorial")
                print("2.Solve Compound Interest")
                print("3.Trigonometric Calculations")
                print("0.Back to Main Menu \n")

                choice=int(input("Enter your choice : "))
                print()

                if choice==1:
                    print("Factorial Calculator : ")
                    num=int(input("Enter your number to convert factorial number : "))
                    print("Factorial : ",(math.factorial(num)))
                    print()

                elif choice==2:
                    p=int(input("Enter Principal Amount : "))
                    r=int(input("Enter Rate of Interest (in %) : "))
                    t=int(input("Enter time (in years) : "))
                    
                    a=p*(1+r/100)**t
                    b=a-p
                    print()
                    print(f"Compound Interest :{b} \n")

                elif choice==3:
                    angle=float(input("Enter angle in degrees : "))
                    print()   
                    one=math.radians(angle)
                        
                    sin=math.sin(angle)
                    cos=math.cos(angle)
                    tan=math.tan(angle)
                        
                    print(f"Sin :{sin} ")
                    print(f"Cos :{cos} ")
                    print(f"Tan : {tan} \n")

                elif choice==0:
                    print("Back to Main Menu ! ")
                    break

                else:
                    print("Your choice is not valid !")  

    elif choice==3:
        while True:
            print("Random Data Generation : \n")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Generate Random OTP")
            print("0. Back to Main Menu\n")
            
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                first=int(input("Enter start number : "))
                second=int(input("Enter end number : "))
                print()
                num=random.randint(first,second)
                print(f"Random number between {first} and {second} : {num} \n")  
                
            elif choice==2:
                fruits = ["apple", "banana", "cherry", "mango"]
                print(random.choice(fruits))
                print()
                
            elif choice==3:
                numbers= random.randint(100000, 999999)
                print()
                print(f"Your OTP is : {numbers} \n" )
                               
            elif choice==0:
                print()
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
    
    elif choice==4:
            print("Generate Unique Indentifiers (UUID):")
            u_id=uuid.uuid4()
            print(f"Generated UUID : {u_id} \n")
                       
    elif choice==5:
        store=[]
        while True:
            print("File Operations (Custom Module) : \n")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("0. Back to Main Menu\n")
                        
            choice=int(input("Enter your choice : ")) 
            print()
            
            if choice==1:
                create=input("Enter your Create file name : ")
                file=open(create,"w")
                file.write("")
                file.close()
                
                store.append(create)
                print()
                print("Your new file is created successfully!\n")   
                
            elif choice==2:
                content=input("Enter your content to Write in the file :  ")
                file=open(create,"w")
                file.write(content)
                file.close()
                store.append(content)
                print()
                print("Your content to write in the file is successfully!\n")
               
            elif choice==3:
                print("File content:")
                file = open(create, "r")
                print(file.readline())
                file.close()
                print()

            elif choice==4:
                added=input("Enter your Update content to Write in the file : ")
                file=open(create,"a")
                file.write(added)
                file.close()
                
                store.append(added)
                print()
                print("your Update content to Write in the file is successfully!\n")
               
            elif choice==0:
                print("Back to Main Menu!")
                break
                
            else:
                print("Your choice is not valid!")
                             
    elif choice==6:
        print("Explore Module Attributes : \n")  
        new=input("Enter module name to explore: ")
        print()
        print(f"Available Attributes in {new} Module : ")
        print(dir(new))
            
    elif choice==7:
        print("Exiting!")
        break
        
    else:
        print("Your choice is not valid!")
        break










