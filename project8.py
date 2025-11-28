import numpy as np
class DataAnalytics:
    arr=None
    
    def create_array(self):
        print("Select the type of array to create : ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array\n")
        
        choice=int(input("Enter your choice : "))
        if choice==1:
            element=list(map(int, input("Enter element (space separated) : ").split()))
            self.array = np.array(element)
            DataAnalytics.arr = self.array
            print("Array created successfully.\n", self.array)
                                            
        elif choice==2:
            row = int(input("Enter the number of rows : "))
            col = int(input("Enter the number of columns : "))
            total = row * col
            elements = list(map(int, input(f"Enter {total} elements for the array separated by space:").split()))
            self.array = np.array(elements).reshape(row, col)
            DataAnalytics.arr = self.array
            print("Array Created Successfully.\n", self.array)
                
        elif choice==3:
            x = int(input("Enter dimension 1 (x): "))
            y = int(input("Enter dimension 2 (y): "))
            z = int(input("Enter dimension 3 (z): "))
            total = x * y * z
            elements = list(map(int, input(f"Enter {total} elements for the 3D array separated by space : ").split()))
            self.array = np.array(elements).reshape(x, y, z)
            DataAnalytics.arr = self.array
            print("Array Created Successfully.\n",self.array)
                    
        else:
            print("Invalid choice!")
            return
    
    def math(self):
        print("Choose a Mathematical Operetions : ")
        print("1. Addition")  
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division\n")
        
        choice=int(input("Enter your choice : "))
        if choice == 1:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("Second Array :")
            print(arr2)
            result = DataAnalytics.arr + arr2
            print("Result of Addition :\n",result)

        elif choice == 2:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("Second Array :")
            print(arr2)
            result = DataAnalytics.arr - arr2
            print("Result of subtraction : \n",result)

        elif choice == 3:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("Second Array :")
            print(arr2)
            result = DataAnalytics.arr * arr2
            print("Result of multiplication : \n",result)

        elif choice == 4:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("Second Array :")
            print(arr2)
            result = DataAnalytics.arr / arr2
            print("Result of division : \n ",result)

        else:
            print("Invalid choice!")
            return
            
    def combin(self):
        print("Choose an option: ")
        print("1. Combine Array")
        print("2. Split Array")

        choice = int(input("Enter your choice : "))
        if choice==1:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("Second Array :")
            print(arr2)
            print("combine array (vertical atack) : ")
            combined = np.concatenate((DataAnalytics.arr, arr2))
            print("Concatenated Array : \n", combined)

        elif choice==2:
            total = DataAnalytics.arr.size
            elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
            parts=int(input("Enter numbers of parts to split array : "))
            print("Original Array :")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
            print("\nSecond Array :")
            print(arr2)
            print("split array : ")
            result = np.split(DataAnalytics.arr, parts)
            print("splitted Array : \n",result )
        else:
            print("Invalid choice!")
            return
        
    def search(self):
        print("Choose an option : ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        
        choice=int(input("Enter your choice: "))
        print()
        if choice==1:
            print("Original Array:")
            print(DataAnalytics.arr)
            print()
            val = int(input("Enter value to search: "))
            result = np.where(DataAnalytics.arr == val)
            print("Found at Index : \n", result)
                
        elif choice == 2:
            while True:
                print("1.Ascending ordered")
                print("2.Descending ordered \n")

                choice=int(input("Enter your choice : "))
                    
                if choice==1:
                    print("Original Array:")
                    print(DataAnalytics.arr)
                    sorted= np.sort(DataAnalytics.arr)
                    print("Ascendig Sorted Array :\n ", sorted)
                    print()
                    return

                elif choice==2:
                    print("Original Array:")
                    print(DataAnalytics.arr)
                    sorted= np.sort(DataAnalytics.arr)[::-1]
                    print("Descending Sorted Array : \n", sorted)
                    print()
                    return
                        
                else:
                    print("Invalid choice !")
                    return

        elif choice == 3:
            x = int(input("Enter value to filter greater than: "))
            filtered= DataAnalytics.arr[DataAnalytics.arr > x]
            print("Filtered Array : \n", filtered)
                
        else:
            print("Invalid choice!")
            return
             
    def aggre(self):
        print("Choose an aggregate/statistical operation :\n ")

        print("1.Aggregate operations")
        print("2.Statistical operations \n")

        choice=int(input("Enter your choice : "))

        if choice==1:
            while True:
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
            
                choice=int(input("Enter your choice : "))
                
                print("Original Array :", DataAnalytics.arr)
                if choice==1:
                    print("Sum :", np.sum(DataAnalytics.arr))
                    
                        
                elif choice == 2:
                    print("Mean :", np.mean(DataAnalytics.arr))
                    
                        
                elif choice == 3:
                    print("Median :", np.median(DataAnalytics.arr))
                    
                    
                elif choice == 4:
                    print("Standard Deviation :", np.std(DataAnalytics.arr))
                    return
                        
                elif choice == 5:
                    print("Variance :", np.var(DataAnalytics.arr))
                    return
                        
                else:
                    print("Invalid choice!")
                    return
        elif choice==2:
            while True:
                print()
                print("1. Minimum values")
                print("2. Maximum values")
                print("3. Percentiles values")
                print("4.corelation of coefficients between arrays \n")

                choice=int(input("Enter your choice : "))
                print()
                
                if choice==1:
                    print("Original Array : \n", DataAnalytics.arr)
                    print("Minimum values :\n", np.min(DataAnalytics.arr))
                    return
                        
                elif choice == 2:
                    print("Original Array : \n", DataAnalytics.arr)
                    print("Maximum values :\n", np.max(DataAnalytics.arr))
                    return

                elif choice == 3:
                    print("Original Array : \n", DataAnalytics.arr)
                    per = float(input("Enter percentile (0-100): "))
                    result = np.percentile(DataAnalytics.arr, per)
                    print(f"{per}th Percentile:", result)
                    

                elif choice == 4:
                    arr2 = list(map(int, input("Enter 1D element array values separated by space:").split()))
                    arr2 = np.array(arr2)
                    arr3 = list(map(int, input("Enter second 1D array values separated by space:").split()))
                    arr3 = np.array(arr2)
                    correlation = np.corrcoef(arr2, arr3)[0, 1]
                    print("Correlation Coefficient:",correlation)
                        
                else:
                    print("Invalid choice!")
                    return
        else:
                    print("Invalid choice!")
                    return

obj = DataAnalytics()   
print("Welcome to the Numpy Analyzer!")
print("="*28)     
while True:
    print()
    print("Choose an option : \n ")
        
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
        
    choice=int(input("Enter your choice : "))
    print()
        
    if choice == 1:
        obj.create_array()

    elif choice == 2:
        obj.math()
               
    elif choice==3:
        obj.combin()
 
    elif choice==4:
        obj.search()

    elif choice==5:
        obj.aggre()  
        
    elif choice==6:
        print("Exit")
        break
    
    else:
        print("Your choice is not valid!")
        break