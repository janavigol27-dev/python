import numpy as np
class DataAnalytics:
    arr=None
    
    def create_array(self):
        print("Select the type of array to create : ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        
        choice=int(input("Enter your choice : "))
        try:
            if choice==1:
                element=list(map(int, input("Enter element (space separated) : ").split()))
                self.array = np.array(element)
                DataAnalytics.arr = self.array
                print("1D Numpy Array:", self.array)
                                            
            elif choice==2:
                row = int(input("Enter the number of rows : "))
                col = int(input("Enter the number of columns : "))
                total = row * col
                elements = list(map(int, input(f"Enter {total} elements for the array separated by space:").split()))
                self.array = np.array(elements).reshape(row, col)
                DataAnalytics.arr = self.array
                print("Array Created Successfully.")
                print(self.array)
                
            elif choice==3:
                x = int(input("Enter dimension 1 (x): "))
                y = int(input("Enter dimension 2 (y): "))
                z = int(input("Enter dimension 3 (z): "))
                total = x * y * z
                elements = list(map(int, input(f"Enter {total} elements for the 3D array separated by space : ").split()))
                self.array = np.array(elements).reshape(x, y, z)
                DataAnalytics.arr = self.array
                print("Array Created Successfully ")
                print(self.array)
                    
            else:
                print("Invalid choice!")
                return
            
        except Exception as e:
            print("Error creating array:", e)

    def math(self):
        print("Choose a Mathematical Operetions : ")
        print("1. Addition")  
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice=int(input("Enter your choice : "))
        try:
            if choice == 1:
                total = DataAnalytics.arr.size
                elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
                print("Original Array :")
                print(DataAnalytics.arr)
                arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
                print("Second Array :")
                print(arr2)
                result = DataAnalytics.arr + arr2
                print("Result of Addition :")
                print(result)

            elif choice == 2:
                total = DataAnalytics.arr.size
                elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
                print("Original Array :")
                print(DataAnalytics.arr)
                arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
                print("\nSecond Array :")
                print(arr2)
                result = DataAnalytics.arr - arr2
                print("Result of subtraction :")
                print(result)

            elif choice == 3:
                total = DataAnalytics.arr.size
                elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
                print("Original Array :")
                print(DataAnalytics.arr)
                arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
                print("\nSecond Array :")
                print(arr2)
                result = DataAnalytics.arr * arr2
                print("Result of multiplication :")
                print(result)

            elif choice == 4:
                total = DataAnalytics.arr.size
                elements2 = list(map(int, input(f"Enter {total} elements for second array:").split()))
                print("Original Array :")
                print(DataAnalytics.arr)
                arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)
                print("\nSecond Array :")
                print(arr2)
                result = DataAnalytics.arr / arr2
                print("Result of division :")
                print(result)

            else:
                print("Invalid choice!")
                return
            
        except Exception as e:
            print("Error creating array:", e)
        
    def combin(self):
        print("Choose an option: ")
        print("1. Combine Array")
        print("2. Split Array")

        choice = int(input("Enter your choice : "))
        try:
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
                print("Concatenated Array:", combined)

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
                print("splitted Array :",result )
            else:
                print("Invalid choice!")
                return
            
        except Exception as e:
            print("Error creating array:", e)   


    def search(self):
        print("Choose an option : ")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        
        choice=int(input("Enter your choice: "))
        try:
            if choice==1:
                val = int(input("Enter value to search: "))
                result = np.where(DataAnalytics.arr == val)
                print("Found at Index:", result)
                
            elif choice == 2:
                print("Original Array:")
                print(DataAnalytics.arr)
                sorted= np.sort(DataAnalytics.arr)
                print("Sorted Array:", sorted)
                                    
            elif choice == 3:
                x = int(input("Enter value to filter greater than: "))
                filtered= DataAnalytics.arr[DataAnalytics.arr > x]
                print("Filtered Array:", filtered)
                
            else:
                print("Invalid choice!")
                return
            
        except Exception as e:
            print("Error creating array:", e)   

    def aggre(self):
        print("Choose an aggregate/statistical operation: ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        
        choice=int(input("Enter your choice : "))
        
        print("Original Array :", DataAnalytics.arr)
        try:
            if choice==1:
                print("Sum:", np.sum(DataAnalytics.arr))
                
            elif choice == 2:
                print("Mean:", np.mean(DataAnalytics.arr))
                
            elif choice == 3:
                print("Median:", np.median(DataAnalytics.arr))
            
            elif choice == 4:
                print("Standard Deviation:", np.std(DataAnalytics.arr))
                
            elif choice == 5:
                print("Variance:", np.var(DataAnalytics.arr))
                
            else:
                print("Invalid choice!")
                return
            
        except Exception as e:
            print("Error creating array:", e)

obj = DataAnalytics()        
while True:
    print("Welcome to the Numpy Analyzer!")
    print("="*28)
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