import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class SalesDataAnalyzer:
    def _init_(self):
        self.data = None

    def __del__(self):
        del self.data
        print("Data deleted from memory!")
        
    def load_dataset(self):
        print("== Load Dataset ==")
        file = input("Enter the path of the dataset (CSV file): ")
        self.data = pd.read_csv(file)
        print("\nDataset Loaded Successfully!\n")
        
    def explore_data(self):
        print("== Explore Dataset ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display Data types")
        print("5. Display basic info")
        
        choice=int(input("Enter your choice : "))

        if choice==1:
            print("== Display the first 5 rows ==")
            print(self.data.head())
            
        elif choice==2:
            print("== Display the last 5 rows ==")        
            print(self.data.tail())
            
        elif choice==3:
            print("== Display column names==") 
            print(self.data.columns.tolist())
            
        elif choice==4:
            print("== Display Data types ==")
            print(self.data.dtypes)
            
        elif choice==5:
            print("== Display basic info ==")
            print(self.data.info())
            
        else:
            print("Your choice is not valid!")
            
    def clean_data(self):
        print("\n===== Perform DataFrame Operations =====")
        print("1. Add Column")
        print("2. Delete Column")
        print("3. Sort Data")
        print("4. Filter Data")
        print("5. Groupby Sum")

        choice=int(input("Enter your choice : "))

        if choice == 1:
            col = input("Enter new column name: ")
            value = input("Enter value to assign: ")
            self.data[col] = value
            print(f"Column '{col}' added successfully!")
        
        elif choice == 2:
            col = input("Enter column name to delete: ")
            if col in self.data.columns:
                del self.data[col]
                print(f"Column '{col}' deleted successfully!")
            else:
                print("Column does not exist!")

        elif choice == 3:
            col = input("Enter column to sort: ")
            if col in self.data.columns:
                order = input("Ascending? (yes/no): ")
                ascending = True if order.lower() == "yes" else False
                self.data = self.data.sort_values(by=col, ascending=ascending)
                print(f"Data sorted by '{col}' successfully!")
            else:
                print("Invalid column name!")

        elif choice== 4:
            col = input("Enter column to filter: ")
            val = input("Enter value: ")

            if col in self.data.columns:
                filtered = self.data[self.data[col] == val]
                print("\n===== FILTERED DATA =====")
                print(filtered)
            else:
                print("Invalid column name!")

        elif choice== 5:
            col = input("Enter column for groupby: ")
            if col in self.data.columns:
                print("\n===== GROUPBY SUM RESULT =====")
                print(self.data.groupby(col).sum())
            else:
                print("Invalid column name!")

        else:
            print("Invalid Option!")


    def handle_missing_data(self):
        print("\n===== Handle Missing Data  =====")
        print("1. Display rows with missing value ")
        print("2. Fill missimg values with Mean")
        print("3. Drop Rows with Missing Values")
        print("4. Replace missing values with a specific value")

        option = int(input("Enter option: "))

        if option == 1:
            print("\nRows containing missing values:")
            print(self.data[self.data.isnull().any(axis=1)])
        
        elif option == 2:
            self.data = self.data.fillna(self.data.mean(numeric_only=True))
            print("\nMissing values filled with column means!")
   
        elif option == 3:
            self.data = self.data.dropna()
            print("\nRows with missing values dropped!")

        elif option == 4:
            value = input("Enter the value to replace missing values: ")
            self.data = self.data.fillna(value)
            print("\nMissing values replaced with:", value)

        else:
            print("Invalid Option!")

    def generate_descriptive_statistics(self):

        print("\n===== Generate Descriptive Statistics =====")
        print("1. Show Summary Statistics (describe)")
        print("2. Show Mean of Each Column")
        print("3. Show Median of Each Column")
        print("4. Show Mode of Each Column")
        print("5. Show Standard Deviation of Each Column")

        option = int(input("Enter option: "))

        if option == 1:
            print("\nSummary Statistics:")
            print(self.data.describe(include="all"))

        elif option == 2:
            print("\nMean of Columns:")
            print(self.data.mean(numeric_only=True))

        elif option == 3:
            print("\nMedian of Columns:")
            print(self.data.median(numeric_only=True))

        elif option == 4:
            print("\nMode of Columns:")
            print(self.data.mode().iloc[0])

        elif option == 5:
            print("\nStandard Deviation:")
            print(self.data.std(numeric_only=True))

        else:
            print("Invalid Option!")

    def data_visualization(self):

        print("\n===== Data Visualization =====")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack plot")

        option = int(input("Enter option: "))

        if option == 1:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            self.data.plot(kind='bar', x=x, y=y)
            plt.title(f"Bar Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
    
        elif option == 2:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            self.data.plot(kind='line', x=x, y=y)
            plt.title(f"Line Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()

        elif option == 3:
            x = input("Enter X-axis column: ")
            y = input("Enter Y-axis column: ")

            plt.scatter(self.data[x], self.data[y])
            plt.title(f"Scatter Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.show()
            
        elif option == 4:
            col = input("Enter column name for Pie Chart: ")

            value_counts = self.data[col].value_counts()

            plt.pie(value_counts, labels=value_counts.index, autopct="%1.1f%%")
            plt.title(f"Pie Chart of {col}")
            plt.show()

        elif option == 5: 
            col = input("Enter column name for Histogram: ")

            plt.hist(self.data[col].dropna())
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()

        elif option == 6:
            col1 = input("Enter first column (X-axis categories): ")
            col2 = input("Enter second column (stacked categories): ")

            cross_tab = pd.crosstab(self.data[col1], self.data[col2])

            cross_tab.plot(kind='bar', stacked=True)
            plt.title(f"Stacked Bar Chart: {col1} vs {col2}")
            plt.xlabel(col1)
            plt.ylabel("Count")
            plt.show()

        else:
            print("Invalid Option!")

    def save_visualization(self):
        print("== Save Visualization ==")
        file = input("Enter file name to save (example: chart.png): ")
        
        plt.savefig(file)     
        print(f"Visualization saved successfully as {file}!")



obj=SalesDataAnalyzer()

while True:
    print("\n========== Data Analysis & Visualization Program ==========\n")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform Dataset Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
            SalesDataAnalyzer.load_dataset()

    elif choice == 2:
       SalesDataAnalyzer.explore_data()

    elif choice == 3:
        SalesDataAnalyzer.clean_data()

    elif choice == 4:
       SalesDataAnalyzer.handle_missing_data()

    elif choice == 5:
        SalesDataAnalyzer.generate_descriptive_statistics()

    elif choice == 6:
        SalesDataAnalyzer.data_visualization()

    elif choice == 7:
           SalesDataAnalyzer.save_visualization()

    elif choice == 8:
        print("Exiting Program... Goodbye!")
        break

    else:
        print("Invalid Choice! Try again.")