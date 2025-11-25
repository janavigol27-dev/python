import numpy as np

class DataAnalytics:
    arr=None
    
    def create_array(self):
        print("Select the type of array to create: ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            ele=list(map(int, input("Enter element (space separated) : ").split()))
            self.array = np.array(ele)
            DataAnalytics.arr = self.array

            print("1D Numpy Array:", self.array)
                                        
        elif choice==2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            total = rows * cols
            print(f"Enter {total} elements for the array separated by space:")

            elements = list(map(int, input().split()))

            self.array = np.array(elements).reshape(rows, cols)
            DataAnalytics.arr = self.array

            print("\nArray Created Successfully ✔")
            print("Your 2D Array is:\n", self.array)
               
        elif choice==3:

            x = int(input("Enter dimension 1 (x): "))
            y = int(input("Enter dimension 2 (y): "))
            z = int(input("Enter dimension 3 (z): "))

            total = x * y * z
            print(f"Enter {total} elements for the 3D array separated by space:")

            elements = list(map(int, input().split()))

            self.array = np.array(elements).reshape(x, y, z)
            DataAnalytics.arr = self.array

            print("\nArray Created Successfully ")
            print("Your 3D Array is:\n", self.array)
                
        else:
            print("Invalid choice!")
            return
            
    def math(self):
        print("choose a Mathematical Operetions : ")
        print("1. Addition")  
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice=int(input("Enter your choice : "))
        
        if choice == 1:
            total = DataAnalytics.arr.size
            print(f"Enter {total} elements for second array:")
            elements2 = list(map(int, input().split()))
             
            print("Original Array:")
            print(DataAnalytics.arr)

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr + arr2
            print("Result of Addition:")
            print(result)

        elif choice == 2:
            total = DataAnalytics.arr.size
            print(f"Enter {total} elements for second array:")
            elements2 = list(map(int, input().split()))
             
            print("Original Array:")
            print(DataAnalytics.arr)

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr - arr2
            print("Result of subtraction :")
            print(result)

        elif choice == 3:
            total = DataAnalytics.arr.size
            print(f"Enter {total} elements for second array:")
            elements2 = list(map(int, input().split()))
             
            print("Original Array:")
            print(DataAnalytics.arr)

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)
            result = DataAnalytics.arr * arr2
            print("Result of multiplication :")
            print(result)

        elif choice == 4:
            total = DataAnalytics.arr.size
            print(f"Enter {total} elements for second array:")
            elements2 = list(map(int, input().split()))
             
            print("Original Array:")
            print(DataAnalytics.arr)

            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            result = DataAnalytics.arr / arr2
            print("Result of division :")
            print(result)


    def combin(self):
        print("Choose an option: ")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice : "))

        if choice==1:
            total = DataAnalytics.arr.size
            print(f"Enter {total} elements for second array:")
            elements2 = list(map(int, input().split()))
            print("Original Array:")
            print(DataAnalytics.arr)
            arr2 = np.array(elements2).reshape(DataAnalytics.arr.shape)

            print("\nSecond Array:")
            print(arr2)

            print("combine array (vertical atack) : ")
            combined = np.concatenate((DataAnalytics, arr2))
            print("Concatenated Array:", combined)



        