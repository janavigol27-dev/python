print()
print("Welcome to the pattern Generator and Number Analyzer !")
sum=0
while True:
    print()
    print("Select an option : ")
    print("1.Generate a pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")

    choice=int(input("Enter your choice : "))

    if choice==1:
        row=int(input("Enter the number of rows for the pattern : "))
        print()
        print("pattern : ")
        for i in range (1,row+1):
            print(("*"*i))

    elif choice==2:
        print()
        start=int(input("Enter the start of the range : " ))
        end=int(input("Enter the end of the range : "))

        for i in range(start,end+1):
            if i%2==0:
                print("Number",i,"is Even")
            else:
                print("Number",i,"is Odd")
            sum=sum+i
        print("Sum of all numbers from",start,"to",end,"is : ",sum)
        print()

    elif choice==3:
        print()
        print("Exiting the program. Goodbye ! ")
        break

    else:
        print()
        print("ypur choice is not valid. ")
        break