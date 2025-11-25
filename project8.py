# print("Welcome to our Numpy Analyzer !")
# print("="*28)

# while True : 
#     print("Choose an option : ")
#     print("1.Creat a Numpy Array")
#     print("2.Perform Mathematical Operations")
#     print("3.Combine orSplit Arrays")
#     print("4.Search, Sort, or Filter Arrays")
#     print("5.Compute Aggregates and Statistics")
#     print("6.Exit \n")

#     choice=int(input("Enter your choice : "))
#     print()

#     if choice==1:
#         while True:
#             print("Select the type of array to areate : ")
#             print("1.1D Array")
#             print("1.2D Array")
#             print("1.3D Array")
#             choice=int(input("Enter your choice : "))
#             print()

#             if choice==1:


                







import numpy as np

class DataAnalyzer:
    arr = None

    def array(self):
        print("Array Creation : ")
        print("1.1D Array")
        print("1.2D Array")
        print("1.3D Array")
        choice=int(input("Enter your choice : "))

        try:
            if choice==1:
                count=list(map(int(input("Enter elements (space separated) : ").split())))
                DataAnalyzer.arr=np.array(count)

                while True:
                    print("Choose an option : ")
                    print("1.Indexing")
                    print("2.Slicing")
                    print("3.Go Back")
                    choice=int(input("Enter your choice : "))
                    print()
                    if choice==1:
                        if DataAnalyzer.arr is None:
                            print("No array created yet ! ")
                            return
                        else:
                            index=tuple(map(int(input("Enter the index (ex: 1 , or 1 2 , or 0 1 2) : ").split())))
                            print("Index value :",DataAnalyzer.arr[index])

                    elif choice==2:
                        if DataAnalyzer.arr is None:
                            print("No array created yet ! ")
                            return
                        else: 
                            print("Enter slicing in this format: end (for 1D) : ")
                            slice=input("Enter slice range : ")
                            result=eval(f"DataAnalytics.arr[{slice}]")
                            print("Sliced output : ",result)
                    elif choice==3:
                        break

                    else:
                        print("Invalid choice !")

            elif choice==2:
                row=int(input("Enter rows : "))
                column=int(input("Enter columns : "))
                count=list(map(int(input("Enter elements (space separated) : ").split())))
                DataAnalyzer.arr=np.array(count).reshape(row,column)

                while True:
                    print("Choose an option : ")
                    print("1.Indexing")
                    print("2.Slicing")
                    print("3.Go Back")
                    choice=int(input("Enter your choice : "))
                    print()
                    if choice==1:
                        if DataAnalyzer.arr is None:
                            print("No array created yet ! ")
                            return
                        else:
                            r=int(input("Enter row index : "))
                            c=int(input("Enter column index : "))
                            print("Index value : ",DataAnalyzer.arr[r,c])

                    elif choice == 2:
                        if DataAnalyzer.arr is None:
                            print("No array created yet ! ")
                            return
                        else:
                            r1=map(int(input("Enter the row range (start:end) : ").split()))
                            c1=map(int(input("Enter the column range (start:end) : ").split()))
                            print("Sliced Array : ",DataAnalyzer.arr[r1,c1])
                    elif choice==3:
                        break

                    else:
                        print("Invalid choice !")
            
            elif choice==3:
                abc=map(int(input("Enter dimensions(x y z) : ").split()))
                count=list(map(int, input("Enter elements (space separated): ").split()))
                DataAnalyzer.arr=np.array(count).reshape(abc)

            else:
                print("Invalid choice ! ")
                return
            print("Array created :\n ",DataAnalyzer.arr)
        except Exception as e:
            print("Error creating Array : ",e)

    def math(self):
        if DataAnalyzer.arr is None:
            print("No array created yet ! ")
            return
        print("Mathematical Operations : ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4.Division")

        first=list(map(int(input("Enter same-size array elements ( space separated) : " ).split())))
        convert=np.array(first)

        print("Origional Array : ",DataAnalyzer.arr)
        print("Second Array : ",convert)

        choice=int(input("Enter your choice : "))
        
        if choice==1:
            print("Result of addition :",DataAnalyzer.arr+convert)
           
        elif choice==2:
            print("Result of subtraction :",DataAnalyzer.arr+convert)

        elif choice==3:
            print("Result of multiplication :",DataAnalyzer.arr+convert)

        elif choice==4:
            print("Result of division :",DataAnalyzer.arr+convert)

        else:
            print("Invalid choice !")

    def combine_arrays(self):
        if DataAnalyzer.arr is None:
            print("No array created yet ! ")
            return
        print("Choose an options : ")
        print("1. Combine Arrays")
        print("2. Split Arrays")

        ch = int(input("Enter your choice : "))

        if ch == 1:
            sec=list(map(int(input("Enter the elements of another array to combine (separated by space) : " ).split())))
            thi=np.array(sec)
            arr1 = np.array(list(map(int, input("Enter 1st 1D array: ").split())))
            arr2 = np.array(list(map(int, input("Enter 2nd 1D array: ").split())))
            print("Combined Array :", np.concatenate((arr1, arr2)))

        elif ch == 2:
            r = int(input("Enter rows : "))
            c = int(input("Enter columns : "))
            arr1 = np.array(list(map(int, input("Enter 1st array elements: ").split()))).reshape(r, c)
            arr2 = np.array(list(map(int, input("Enter 2nd array elements: ").split()))).reshape(r, c)

            print("How to combine?")
            print("1. Row-wise (axis=0)")
            print("2. Column-wise (axis=1)")
            sub = int(input("Enter your choice : "))

            if sub == 1:
                print("Combined Array :\n", np.concatenate((arr1, arr2), axis=0))
            else:
                print("Combined Array :\n", np.concatenate((arr1, arr2), axis=1))

        else:
            print("Invalid choice!")

    def split_array(self):
        print("Split Array")
        arr = np.array(list(map(int, input("Enter array elements: ").split())))
        n = int(input("Enter number of equal parts : "))

        print("Splitted Arrays :", np.array_split(arr, n))



print("Welcome to our Numpy Analyzer !")
print("="*28)

obj=DataAnalyzer() 

while True : 
    print("Choose an option : ")
    print("1.Creat a Numpy Array")
    print("2.Perform Mathematical Operations")
    print("3.Combine orSplit Arrays")
    print("4.Search, Sort, or Filter Arrays")
    print("5.Compute Aggregates and Statistics")
    print("6.Exit \n")

    choice=int(input("Enter your choice : "))
    print()

    if choice==1:
        # obj=DataAnalyzer()
        obj.array()