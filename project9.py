import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class SalesDataAnalyzer:
    def _init_(self):
        self.data = None
        
    def load_dataset(self):
        print("\n == Load Dataset ==\n")
        file = input("Enter the path of the dataset (CSV file): ")
        try:
            self.data = pd.read_csv(file)
            print("\nDataset Loaded Successfully!\n")
        except FileNotFoundError:
            print("ERROR: File Not Found. Please enter correct path.")
        
    def explore_data(self):
        print("\n== Explore Dataset ==\n")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display Data types")
        print("5. Display basic info")
        
        choice=int(input("Enter your choice : "))

        if choice==1:
            print("\n== Display the first 5 rows ==\n")
            print(self.data.head())
            
        elif choice==2:
            print("\n== Display the last 5 rows ==\n")        
            print(self.data.tail())
            
        elif choice==3:
            print("\n== Display column names==\n") 
            print(self.data.columns.tolist())
            
        elif choice==4:
            print("\n== Display Data types ==\n")
            print(self.data.dtypes)
            
        elif choice==5:
            print("\n== Display basic info ==\n")
            print(self.data.info())
            
        else:
            print("Your choice is not valid!\n")
            
    def clean_data(self):
        print("\n== Perform Dataset Operations ==\n")
        print("1. Add Column")
        print("2. Delete Column")
        print("3. Sort Data")
        print("4. Filter Data")
        print("5. Groupby Sum\n")     
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            print("\n== Add Column ==\n")
            col = input("Enter new column name: ")
            value = input("Enter value to assign: ")
            self.data[col] = value
            print(f"\nColumn '{col}' added successfully!\n")
            
        elif choice==2:
            print("\n== Delete Column ==\n")
            col = input("Enter column name to delete : ")
            if col in self.data.columns:
                del self.data[col]
                print(f"\nColumn '{col}' deleted successfully!\n")
            else:
                print("Column does not exist!\n")
                
        elif choice == 3:
            print("\n== Sort Data ==\n")
            col = input("Enter column to sort : ")
            if col in self.data.columns:
                self.data = self.data.sort_values(by=col, ascending=True)
                print(f"\nData sorted by '{col}' in ascending order successfully !\n")
            else:
                print("Invalid column name!\n")
                
        elif choice==4:
            print("\n== Filter Data ==\n") 
            col = input("Enter column to filter: ")
            val = input("Enter value: ")

            if col in self.data.columns:
                filtered = self.data[self.data[col] == val]
                print(filtered)
            else:
                print("Invalid column name!\n")
                
        elif choice==5:
            print("\n== Groupby Sum ==\n")  
            col = input("Enter column for groupby: ")
            if col in self.data.columns:
                print("\n===== GROUPBY SUM RESULT =====\n")
                print(self.data.groupby(col).sum())
            else:
                print("Invalid column name!\n")

        else:
            print("Your choice is not valid!\n")
        
    def handle_missing_data(self):
        print("\n== Handle Missing Data ==\n")
        print("1. Display rows with missing value")
        print("2. Fill missing value with mean")
        print("3. Drop rows with missing value")
        print("4. Replace missing value with a specific value\n")
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            print("\n== Display rows with missing value ==\n")
            print(self.data[self.data.isnull().any(axis=1)])
            
        elif choice==2:
            print("\n== Fill missing value with mean ==\n")
            self.data = self.data.fillna(self.data.mean(numeric_only=True))        
        
        elif choice==3:
            print("\n== Drop rows with missing value ==\n")
            self.data = self.data.dropna()  
            
        elif choice==4:
            print("\n== Replace missing value with a specific value ==\n")
            value = input("Enter the value to replace missing values: ")
            self.data = self.data.fillna(value)
            print("\nMissing values replaced with:", value,"\n")                                

        else:
            print("Your choice is not valid!\n")
            return

    def generate_descriptive_statistics(self):
        print("\n== Generate Descriptive Statistics ==\n")
        print("1. Show Summary Statistics (describe)")
        print("2. Show Mean of Each Column")
        print("3. Show Median of Each Column")
        print("4. Show Mode of Each Column")
        print("5. Show Standard Deviation of Each Column\n")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("\n== Show Summary Statistics (describe) ==\n")
            print(self.data.describe(include="all"))

        elif choice == 2:
            print("\n== Show Mean of Each Column ==\n")
            print(self.data.mean(numeric_only=True))

        elif choice == 3:
            print("\n== Show Median of Each Column ==\n")
            print(self.data.median(numeric_only=True))

        elif choice == 4:
            print("\n== Show Mode of Each Column ==\n")
            print(self.data.mode().iloc[0])

        elif choice == 5:
            print("\n== Show Standard Deviation of Each Column ==\n")
            print(self.data.std(numeric_only=True))
            
        else:
            print("Your choice is not valid!\n")
            return
    
    def data_visualization(self):
        print("\n== Data Visualization ==\n")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot\n")
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            print("\n== Bar Plot ==\n")
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            self.data.plot(kind='bar', x=x, y=y)
            plt.title(f"Bar Plot of {y} vs {x} ")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()           
                
        elif choice==2:
            print("\n== Line Plot ==\n")
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            self.data.plot(kind='line', x=x, y=y)
            plt.title(f"Line Plot of {y} vs {x} ")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()            
                
        elif choice==3:
            print("\n== Scatter Plot ==\n")
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            plt.scatter(self.data[x], self.data[y])
            plt.title(f"Scatter Plot of {y} vs {x} ")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()           
                                        
        elif choice==4:
            print("\n== Pie Plot ==\n")
            col = input("Enter column name for Pie Chart: ")
            value_counts = self.data[col].value_counts()
            plt.pie(value_counts, labels=value_counts.index, autopct="%1.1f%%")
            plt.title(f"Pie Chart of {col} ")
            plt.show()
            
        elif choice==5:
            print("\n== Histogram ==\n")
            col = input("Enter column name for Histogram: ")

            plt.hist(self.data[col].dropna())
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()            
                    
        elif choice==6:
            print("\n== Stack Plot ==\n")
            col1 = input("Enter first column (X-axis categories): ")
            col2 = input("Enter second column (stacked categories): ")

            cross_tab = pd.crosstab(self.data[col1], self.data[col2])

            cross_tab.plot(kind='bar', stacked=True)
            plt.title(f"Stacked Bar Chart: {col1} vs {col2}")
            plt.xlabel(col1)
            plt.ylabel("Count")
            plt.show()    
                  
        else:
            print("Your choice is not valid!\n")
            return              
                    
    def save_visualization(self):
        print("\n== Save Visualization ==\n")
        file = input("Enter file name to save the plot (example: scatter_plot.png): ")      
        plt.savefig(file)      
        print(f"\nVisualization saved successfully as {file}! \n")
        
    def indexing_values(self):
        print("\n== Indexing, Slicing and Pivot tabel ==\n")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Pivot tabel\n")
        
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            print("\n== Indexing ==\n")
            print("Available Columns:", list(self.data.columns))

            row = int(input("Enter row index: "))
            col = input("Enter column name: ")

            result = self.data.loc[row, col]
            print(f"\nValue at [{row}] and '{col}' is: {result}")
            
        elif choice==2:
            print("\n== Slicing ==\n")
            print("Available Columns:", list(self.data.columns))

            start = int(input("Enter start row index: "))
            end = int(input("Enter end row index: "))
            col = input("Enter column name: ")

            result = self.data.loc[start:end, col]
            print(f"\nSliced data from row {start} to {end} for column '{col}':\n")
            print(result)
          
        elif choice==3:
            print("\n== Pivot Table ==\n")
            print("Available Columns:", list(self.data.columns))

            index_col = input("Enter column for rows (index): ")
            column_col = input("Enter column for columns: ")
            values_col = input("Enter column for values: ")

            result = self.data.pivot_table(index=index_col, columns=column_col, values=values_col, aggfunc='sum')
            print("\nPivot Table:\n")
            print(result)
            
        else:
            print("Your choice is not valid!\n")
            return
    
    def _del_(self):
        del self.data

obj=SalesDataAnalyzer()

while True:
    print("="*8,"Data Analysis & Visualization Program","="*8)
    
    print("Please select an option:")

    print("1. Load Dataset")
    print("2. Explore Data")    
    print("3. Perform Dataset Operations")
    print("4. Handle Missing Date")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Indexing, Slicing and Pivot tabel")
    print("9. Exit")
    print("="*30)

    choice=int(input("Enter your choice : "))
    
    if choice==1:
        obj.load_dataset()
        
    elif choice==2:
        obj.explore_data()
        
    elif choice==3:
        obj.clean_data()
        
    elif choice==4:
        obj.handle_missing_data()
        
    elif choice==5:
        obj.generate_descriptive_statistics()
        
    elif choice==6:
        obj.data_visualization()
        
    elif choice==7:
        obj.save_visualization()
        
    elif choice==8:
        obj.indexing_values()
        
    elif choice==9:
        print("Exiting \n")
        break
        
    else:
        print("Your choice is not valid! \n")
        break