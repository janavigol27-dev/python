# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# class SalesDataAnalyzer:

#     # 1️⃣ Load dataset
#     def __init__(self):
#         self.file = input("Enter your CSV file path : ")
#         self.data = pd.read_csv(self.file)
#         print("\nDataset Loaded Successfully!\n")

#     def __del__(self):
#         del self.data
#         print("Data deleted from memory!")

#     # 2️⃣ Explore dataset
#     def explore_data(self):
#         print("\n===== BASIC INFORMATION =====")
#         print(self.data.info())

#         print("\n===== FIRST 5 ROWS =====")
#         print(self.data.head())

#         print("\n===== LAST 5 ROWS =====")
#         print(self.data.tail())

#         print("\n===== DATA SHAPE =====")
#         print(f"Rows: {self.data.shape[0]}, Columns: {self.data.shape[1]}")

#         print("\n===== COLUMNS =====")
#         print(self.data.columns.tolist())

#         print("\n===== MISSING VALUES =====")
#         print(self.data.isnull().sum())

#         print("\n===== SUMMARY STATISTICS =====")
#         print(self.data.describe())
#         print()

#     # 3️⃣ Handle Missing Data
#     def handle_missing_data(self):
#         print("\n===== Missing Data Summary =====")
#         print(self.data.isnull().sum())

#         print("\nChoose how to handle missing values:")
#         print("1. Fill with Mean")
#         print("2. Fill with Median")
#         print("3. Fill with Mode")
#         print("4. Drop Rows with Missing Values")
#         print("5. Drop Columns with Missing Values")

#         option = int(input("Enter option: "))

#         column = None
#         if option in [1, 2, 3]:
#             column = input("Enter column name: ")
#             if column not in self.data.columns:
#                 print("Invalid Column!")
#                 return

#         if option == 1:
#             self.data[column].fillna(self.data[column].mean(), inplace=True)
#             print(f"Missing values in '{column}' filled with MEAN.")

#         elif option == 2:
#             self.data[column].fillna(self.data[column].median(), inplace=True)
#             print(f"Missing values in '{column}' filled with MEDIAN.")

#         elif option == 3:
#             self.data[column].fillna(self.data[column].mode()[0], inplace=True)
#             print(f"Missing values in '{column}' filled with MODE.")

#         elif option == 4:
#             self.data.dropna(inplace=True)
#             print("Rows containing missing values DROPPED.")

#         elif option == 5:
#             self.data.dropna(axis=1, inplace=True)
#             print("Columns containing missing values DROPPED.")

#         else:
#             print("Invalid Option!")

#     # 4️⃣ Add new column
#     def add_column(self, new_col, value):
#         self.data[new_col] = value
#         print(f"Column '{new_col}' added!")

#     # 5️⃣ Delete column
#     def delete_column(self, col):
#         if col in self.data.columns:
#             del self.data[col]
#             print(f"Column '{col}' deleted!")
#         else:
#             print("Column does not exist!")

#     # 6️⃣ Sort Data
#     def sort_data(self, column, ascending=True):
#         if column in self.data.columns:
#             self.data = self.data.sort_values(by=column, ascending=ascending)
#             print(f"Data sorted by '{column}'.")
#         else:
#             print("Column not found!")

#     # 7️⃣ Filter Data
#     def filter_data(self, column, value):
#         if column in self.data.columns:
#             filtered = self.data[self.data[column] == value]
#             print("\n===== FILTERED DATA =====")
#             print(filtered)
#         else:
#             print("Column not found!")

#     # 8️⃣ Groupby Sum
#     def groupby_sum(self, column):
#         if column in self.data.columns:
#             print("\n===== GROUPBY RESULT =====")
#             print(self.data.groupby(column).sum())
#         else:
#             print("Column not found!")

#     # 9️⃣ Correlation Heatmap
#     def show_correlation(self):
#         print("\n===== CORRELATION MATRIX =====")
#         print(self.data.corr())

#         plt.figure(figsize=(8, 5))
#         sns.heatmap(self.data.corr(), annot=True)
#         plt.title("Correlation Heatmap")
#         plt.show()

#     # 🔟 Descriptive Statistics
#     def descriptive_stats(self):
#         print("\n===== DESCRIPTIVE STATISTICS =====")
#         print(self.data.describe())

#         # 🔟 Advanced Descriptive Statistics Function
#     def generate_descriptive_stats(self):
#         print("\n========== ADVANCED DESCRIPTIVE STATISTICS ==========\n")

#         numeric_cols = self.data.select_dtypes(include=np.number).columns

#         if len(numeric_cols) == 0:
#             print("No numeric columns available for descriptive statistics!")
#             return

#         print("Numeric Columns:", list(numeric_cols))

#         print("\n===== BASIC DESCRIBE() OUTPUT =====")
#         print(self.data[numeric_cols].describe())

#         print("\n===== MEAN VALUES =====")
#         print(self.data[numeric_cols].mean())

#         print("\n===== MEDIAN VALUES =====")
#         print(self.data[numeric_cols].median())

#         print("\n===== MODE VALUES =====")
#         print(self.data[numeric_cols].mode().iloc[0])

#         print("\n===== VARIANCE =====")
#         print(self.data[numeric_cols].var())

#         print("\n===== STANDARD DEVIATION =====")
#         print(self.data[numeric_cols].std())

#         print("\n===== SKEWNESS =====")
#         print(self.data[numeric_cols].skew())

#         print("\n===== KURTOSIS =====")
#         print(self.data[numeric_cols].kurt())

#         print("\n========== END ==========\n")



# # ==========================================
# #          MENU-DRIVEN PROGRAM
# # ==========================================

# analyzer = None

# while True:
#     print("\n========== Data Analysis & Visualization Program ==========\n")
#     print("1. Load Dataset")
#     print("2. Explore Data")
#     print("3. Perform Dataset Operations")
#     print("4. Handle Missing Data")
#     print("5. Generate Descriptive Statistics")
#     print("6. Data Visualization")
#     print("7. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         analyzer = SalesDataAnalyzer()

#     elif choice == 2:
#         if analyzer:
#             analyzer.explore_data()
#         else:
#             print("Please load dataset first!")

#     elif choice == 3:
#         if analyzer:
#             print("\n1. Add Column")
#             print("2. Delete Column")
#             print("3. Sort Data")
#             print("4. Filter Data")
#             print("5. Groupby Sum")

#             op = int(input("Enter option: "))

#             if op == 1:
#                 c = input("Enter new column name: ")
#                 v = input("Enter value to assign: ")
#                 analyzer.add_column(c, v)

#             elif op == 2:
#                 c = input("Enter column name to delete: ")
#                 analyzer.delete_column(c)

#             elif op == 3:
#                 c = input("Enter column to sort: ")
#                 order = input("Ascending? (yes/no): ")
#                 analyzer.sort_data(c, ascending=(order.lower() == "yes"))

#             elif op == 4:
#                 c = input("Enter column to filter: ")
#                 v = input("Enter value: ")
#                 analyzer.filter_data(c, v)

#             elif op == 5:
#                 c = input("Enter column for groupby: ")
#                 analyzer.groupby_sum(c)

#         else:
#             print("Please load dataset first!")

#     elif choice == 4:
#         if analyzer:
#             analyzer.handle_missing_data()
#         else:
#             print("Please load dataset first!")

#     elif choice == 5:
#         if analyzer:
#             analyzer.descriptive_stats()
#         else:
#             print("Please load dataset first!")

#     elif choice == 6:
#         if analyzer:
#             analyzer.show_correlation()
#         else:
#             print("Please load dataset first!")

#     elif choice == 7:
#         print("Exiting Program...")
#         break

#     else:
#         print("Invalid Choice! Try again.")








import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    # 1️⃣ Load dataset
    def __init__(self):
        self.file = input("Enter your CSV file path : ")
        self.data = pd.read_csv(self.file)
        print("\nDataset Loaded Successfully!\n")

    def __del__(self):
        del self.data
        print("Data deleted from memory!")

    # 2️⃣ Explore dataset
    def explore_data(self):
        print("\n===== BASIC INFORMATION =====")
        print(self.data.info())

        print("\n===== FIRST 5 ROWS =====")
        print(self.data.head())

        print("\n===== LAST 5 ROWS =====")
        print(self.data.tail())

        print("\n===== DATA SHAPE =====")
        print(f"Rows: {self.data.shape[0]}, Columns: {self.data.shape[1]}")

        print("\n===== COLUMNS =====")
        print(self.data.columns.tolist())

        print("\n===== MISSING VALUES =====")
        print(self.data.isnull().sum())

        print("\n===== SUMMARY STATISTICS =====")
        print(self.data.describe())
        print()

    # 3️⃣ Handle Missing Data
    def handle_missing_data(self):
        print("\n===== Missing Data Summary =====")
        print(self.data.isnull().sum())

        print("\nChoose how to handle missing values:")
        print("1. Fill with Mean")
        print("2. Fill with Median")
        print("3. Fill with Mode")
        print("4. Drop Rows with Missing Values")
        print("5. Drop Columns with Missing Values")

        option = int(input("Enter option: "))

        column = None
        if option in [1, 2, 3]:
            column = input("Enter column name: ")
            if column not in self.data.columns:
                print("Invalid Column!")
                return

        if option == 1:
            self.data[column].fillna(self.data[column].mean(), inplace=True)
            print(f"Missing values in '{column}' filled with MEAN.")

        elif option == 2:
            self.data[column].fillna(self.data[column].median(), inplace=True)
            print(f"Missing values in '{column}' filled with MEDIAN.")

        elif option == 3:
            self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            print(f"Missing values in '{column}' filled with MODE.")

        elif option == 4:
            self.data.dropna(inplace=True)
            print("Rows containing missing values DROPPED.")

        elif option == 5:
            self.data.dropna(axis=1, inplace=True)
            print("Columns containing missing values DROPPED.")

        else:
            print("Invalid Option!")

    # 4️⃣ Add new column
    def add_column(self, new_col, value):
        self.data[new_col] = value
        print(f"Column '{new_col}' added!")

    # 5️⃣ Delete column
    def delete_column(self, col):
        if col in self.data.columns:
            del self.data[col]
            print(f"Column '{col}' deleted!")
        else:
            print("Column does not exist!")

    # 6️⃣ Sort Data
    def sort_data(self, column, ascending=True):
        if column in self.data.columns:
            self.data = self.data.sort_values(by=column, ascending=ascending)
            print(f"Data sorted by '{column}'.")
        else:
            print("Column not found!")

    # 7️⃣ Filter Data
    def filter_data(self, column, value):
        if column in self.data.columns:
            filtered = self.data[self.data[column] == value]
            print("\n===== FILTERED DATA =====")
            print(filtered)
        else:
            print("Column not found!")

    # 8️⃣ Groupby Sum
    def groupby_sum(self, column):
        if column in self.data.columns:
            print("\n===== GROUPBY RESULT =====")
            print(self.data.groupby(column).sum())
        else:
            print("Column not found!")

    # 9️⃣ Correlation Heatmap
    def show_correlation(self):
        print("\n===== CORRELATION MATRIX =====")
        print(self.data.corr())

        plt.figure(figsize=(8, 5))
        sns.heatmap(self.data.corr(), annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    # 🔟 Descriptive Statistics
    def descriptive_stats(self):
        print("\n===== DESCRIPTIVE STATISTICS =====")
        print(self.data.describe())

    # 🔟 Advanced Descriptive Statistics Function
    def generate_descriptive_stats(self):
        print("\n========== ADVANCED DESCRIPTIVE STATISTICS ==========\n")

        numeric_cols = self.data.select_dtypes(include=np.number).columns

        if len(numeric_cols) == 0:
            print("No numeric columns available for descriptive statistics!")
            return

        print("Numeric Columns:", list(numeric_cols))

        print("\n===== BASIC DESCRIBE() OUTPUT =====")
        print(self.data[numeric_cols].describe())

        print("\n===== MEAN VALUES =====")
        print(self.data[numeric_cols].mean())

        print("\n===== MEDIAN VALUES =====")
        print(self.data[numeric_cols].median())

        print("\n===== MODE VALUES =====")
        print(self.data[numeric_cols].mode().iloc[0])

        print("\n===== VARIANCE =====")
        print(self.data[numeric_cols].var())

        print("\n===== STANDARD DEVIATION =====")
        print(self.data[numeric_cols].std())

        print("\n===== SKEWNESS =====")
        print(self.data[numeric_cols].skew())

        print("\n===== KURTOSIS =====")
        print(self.data[numeric_cols].kurt())

        print("\n========== END ==========\n")

    # 1️⃣1️⃣ Visualization Function
    def visualize_data(self):
        print("\n===== Visualization Options =====")
        print("1. Histogram")
        print("2. Bar Plot")
        print("3. Line Plot")
        print("4. Count Plot")

        choice = int(input("Enter your choice : "))

        col = input("Enter column name : ")

        if col not in self.data.columns:
            print("Invalid Column!")
            return

        plt.figure(figsize=(8, 5))

        if choice == 1:
            plt.hist(self.data[col].dropna())
            plt.title(f"Histogram of {col}")

        elif choice == 2:
            sns.barplot(x=self.data[col].value_counts().index,
                        y=self.data[col].value_counts().values)
            plt.title(f"Bar Plot of {col}")

        elif choice == 3:
            plt.plot(self.data[col])
            plt.title(f"Line Plot of {col}")

        elif choice == 4:
            sns.countplot(x=self.data[col])
            plt.title(f"Count Plot of {col}")

        else:
            print("Invalid option!")
            return

        plt.show()

    # 1️⃣2️⃣ Save Visualization
    def save_visualization(self):
        col = input("Enter column name to visualize and save: ")

        if col not in self.data.columns:
            print("Invalid Column!")
            return

        plt.figure(figsize=(8, 5))
        plt.hist(self.data[col].dropna())
        plt.title(f"Histogram of {col}")

        filename = input("Enter file name to save (example: graph.png) : ")
        plt.savefig(filename)

        print(f"Visualization saved as {filename}")


# ==========================================
#          MENU-DRIVEN PROGRAM
# ==========================================

analyzer = None

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
        analyzer = SalesDataAnalyzer()

    elif choice == 2:
        if analyzer:
            analyzer.explore_data()
        else:
            print("Please load dataset first!")

    elif choice == 3:
        if analyzer:
            print("\n1. Add Column")
            print("2. Delete Column")
            print("3. Sort Data")
            print("4. Filter Data")
            print("5. Groupby Sum")

            op = int(input("Enter option: "))

            if op == 1:
                c = input("Enter new column name: ")
                v = input("Enter value to assign: ")
                analyzer.add_column(c, v)

            elif op == 2:
                c = input("Enter column name to delete: ")
                analyzer.delete_column(c)

            elif op == 3:
                c = input("Enter column to sort: ")
                order = input("Ascending? (yes/no): ")
                analyzer.sort_data(c, ascending=(order.lower() == "yes"))

            elif op == 4:
                c = input("Enter column to filter: ")
                v = input("Enter value: ")
                analyzer.filter_data(c, v)

            elif op == 5:
                c = input("Enter column for groupby: ")
                analyzer.groupby_sum(c)

    elif choice == 4:
        if analyzer:
            analyzer.handle_missing_data()
        else:
            print("Please load dataset first!")

    elif choice == 5:
        if analyzer:
            print("\n1. Basic Descriptive Statistics")
            print("2. Advanced Descriptive Statistics")

            stats_choice = int(input("Enter option: "))

            if stats_choice == 1:
                analyzer.descriptive_stats()
            elif stats_choice == 2:
                analyzer.generate_descriptive_stats()
            else:
                print("Invalid option!")
        else:
            print("Please load dataset first!")

    elif choice == 6:
        if analyzer:
            analyzer.visualize_data()
        else:
            print("Please load dataset first!")

    elif choice == 7:
        if analyzer:
            analyzer.save_visualization()
        else:
            print("Please load dataset first!")

    elif choice == 8:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try again.")













# 1️⃣3️⃣ Perform DataFrame Operations Using def
    def perform_dataframe_operations(self):
        print("\n===== DataFrame Operations =====")
        print("1. Add Column")
        print("2. Delete Column")
        print("3. Sort Data")
        print("4. Filter Data")
        print("5. Groupby Sum")

        op = int(input("Enter option: "))

        # 1️⃣ Add Column
        if op == 1:
            col = input("Enter new column name: ")
            value = input("Enter value to assign: ")
            self.data[col] = value
            print(f"Column '{col}' added successfully!")

        # 2️⃣ Delete Column
        elif op == 2:
            col = input("Enter column name to delete: ")
            if col in self.data.columns:
                del self.data[col]
                print(f"Column '{col}' deleted successfully!")
            else:
                print("Column does not exist!")

        # 3️⃣ Sort Data
        elif op == 3:
            col = input("Enter column to sort: ")
            if col in self.data.columns:
                order = input("Ascending? (yes/no): ")
                ascending = True if order.lower() == "yes" else False
                self.data = self.data.sort_values(by=col, ascending=ascending)
                print(f"Data sorted by '{col}' successfully!")
            else:
                print("Invalid column name!")

        # 4️⃣ Filter Data
        elif op == 4:
            col = input("Enter column to filter: ")
            val = input("Enter value: ")

            if col in self.data.columns:
                filtered = self.data[self.data[col] == val]
                print("\n===== FILTERED DATA =====")
                print(filtered)
            else:
                print("Invalid column name!")

        # 5️⃣ Groupby Sum
        elif op == 5:
            col = input("Enter column for groupby: ")
            if col in self.data.columns:
                print("\n===== GROUPBY SUM RESULT =====")
                print(self.data.groupby(col).sum())
            else:
                print("Invalid column name!")

        else:
            print("Invalid Option!")