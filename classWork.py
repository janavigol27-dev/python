# input \ output function :
# print(34)
# print(34+34)
# print("34+34") 
# print("first value",34,"value is very strong.")


# variable -> this is a container to used to store some value.

# varible true name rules :
# name -True
# 34 - False
# $ - False
# ab-cd - False
# name_var - True

# input :
# input("enter your name : ")
# print("hello")

# a=46
# b=10
# print(a-b)
# print(a+b)
# print(a*b)
# print(a/b)
# print(a%b)



# file=open("demo.txt","r")
# contant=file.read()
# print(contant)
# file.close()


file=open("demo.txt","w")
file.write("")
file.close()


# file = open("sample.txt", "w")  # Open file in write mode
# file.write("Hello, Python!")  # Writing content
# file.close()  # Closing the file


print("Date Formatting : \n")
                date=input("Enter date (YYYY-MM-DD) : ")
                date=datetime.strptime(date,"%Y-%m-%d")
                print("1.DD-MM-YYYY")
                print("2.MM-DD-YYYY")
                print("3.YYYY-MM-DD")
                print("4.DD MM YYYY")
                print("MM DD,YYYY \n")

                choice=int(input("Choose formate : "))
                print()

                if choice==1:
                    print(date.strftime("%d-%m-%Y"))
                elif choice==2:
                    print(date.strftime("%m-%d-%Y"))
                elif choice==3:
                    print(date.strftime("%Y-%m-%d"))
