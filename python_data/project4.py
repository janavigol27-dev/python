def factorial(e):
    fact=1
    for i in range(2,e+1):
        fact*=i
    return fact


print("Welcome to the Data Analyzer and Transformer program.")
print()
li=[]
while True:
    print("Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary (Built-in Functions)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7.Exit program")
    print()
    choice=int(input("Please enter your choice: "))
    print()
    if choice==1:
        a=input("Enter data for a 1D array (Separated by spaces) : ")
        for i in a.split():
            li.append(int(i))
        print()
        print("Data has been stored successfully! \n")
    elif choice==2:
        print("Data Summery :")
        print(f"-Total elements : {len(li)}")
        print(f"-Minimum Value : {min(li)}")
        print(f"-Maximum Value : {max(li)}")
        print(f"-Sum of all Values : {sum(li)}")
        print(f"-Average Value :{sum(li)/len(li)} \n")
        
    elif choice==3:
        e=int(input("Enter a number to calculate its factorial : "))
        print()
        print(f"Factorial of {e} is : {factorial(e)}")
        print()

    elif choice==4:
        f=int(input("Enter a threshold value to filter out data above this value : " ))
        g=[i for i in li if i>f]
        print()
        print(f"Filtered Data (values >= {f}) : {g} \n")

    elif choice==5:
        print("Choose sorting option : ")
        print("1.Ascending")
        print("2.Descending")
        print()
        h=int(input("Enter your choice : "))
        print()
        if h==1:
            li.sort()
            print(f"Sorted Data in Ascending Order : {li} \n ")
        elif h==2:
            li.sort(reverse=True)
            print(f"Sorted Data in Descending Order : {li} \n ")
        else:
            print("No data available.")
    
    elif choice==6:
        print("Dataset Statistics : ")
        print(f"-Minimum value : {min(li)} ")
        print(f"Maximum value :{max(li)} ")
        print(f"Sum of all value :{sum(li)} ")
        print(f"Average value :{sum(li)/len(li)} \n ")

    elif choice==7:
        print("Thank you for using the Data Analyzer and Transformer program. Goodbye! \n")
        break
    
    else:
        print("Your choice is not valid.")
        break




