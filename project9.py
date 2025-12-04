import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.file=input("Enter your CSV file path : ")
        self.data=pd.read_csv(self.file)
        print()

    def __del__ (self):
        del self.data
        print("Data deleted from memory!")

    def explore_data(self):
        print("===== BASIC INFORMATION =====")
        print(self.data.info())
        print("\n")

        print("===== FIRST 5 ROWS =====")
        print(self.data.head())
        print("\n")

        print("===== LAST 5 ROWS =====")
        print(self.data.tail())
        print("\n")

        print("===== SHAPE OF DATA =====")
        print(f"Rows: {self.data.shape[0]}, Columns: {self.data.shape[1]}")
        print("\n")

        print("===== COLUMNS =====")
        print(self.data.columns.tolist())
        print("\n")

        print("===== MISSING VALUES =====")
        print(self.data.isnull().sum())
        print("\n")

        print("===== SUMMARY STATISTICS =====")
        print(self.data.describe())
        print("\n")

    def fill_missing(self, column):
        if column in self.data.columns:
            self.data[column].fillna(self.data[column].mean(), inplace=True)
            print(f"Missing values in '{column}' filled with mean.")
        else:
            print("Column not found!")

    # 3️⃣ Add new column
    def add_column(self, new_col, value):
        self.data[new_col] = value
        print(f"Column '{new_col}' added successfully!")

    # 4️⃣ Delete column
    def delete_column(self, col):
        if col in self.data.columns:
            del self.data[col]
            print(f"Column '{col}' deleted!")
        else:
            print("Column does not exist!")

    # 5️⃣ Sort DataFrame
    def sort_data(self, column, ascending=True):
        if column in self.data.columns:
            self.data = self.data.sort_values(by=column, ascending=ascending)
            print(f"Data sorted by '{column}', ascending = {ascending}")
        else:
            print("Column not found!")

    # 6️⃣ Filter rows
    def filter_data(self, column, value):
        if column in self.data.columns:
            filtered = self.data[self.data[column] == value]
            print(f"Filtered data where {column} = {value}:")
            print(filtered)
        else:
            print("Column not found!")

    # 7️⃣ Groupby operation
    def groupby_sum(self, column):
        if column in self.data.columns:
            print(f"Sum of values group by '{column}':")
            print(self.data.groupby(column).sum())
        else:
            print("Column not found!")

    # 8️⃣ Correlation
    def show_correlation(self):
        print("Correlation Matrix:")
        print(self.data.corr())

        plt.figure(figsize=(8, 5))
        sns.heatmap(self.data.corr(), annot=True)
        plt.title("Correlation Heatmap")
        plt.show()








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
    print("8. Exit")

    choice=int(input("Enter your choice : "))