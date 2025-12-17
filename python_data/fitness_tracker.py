import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class FitnessDashboard:
    def __init__(self, filename="gym_members_exercise_tracking_synthetic_data.csv"):
        self.filename = filename
        try:
            self.listt = pd.read_csv(filename)
        except FileNotFoundError:
            self.listt = pd.DataFrame(columns=["Date", "Workout", "Time (Minutes)", "Calories"])
            self.listt.to_csv(filename, index=False)

    def add_entry(self, workout, timespent, caloriesburned):
        if timespent <= 0 or caloriesburned <= 0:
            print(" Time and calories must be greater than zero !")
            return

        loged = {
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Workout": workout,
            "Time (Minutes)": timespent,
            "Calories": caloriesburned
        }

        self.listt = pd.concat([self.listt, pd.DataFrame([loged])], ignore_index=True)
        self.listt.to_csv(self.filename, index=False)
        print(f"Added: {workout} - {timespent} mins, {caloriesburned} cal")

    def show_summary(self):
        if self.listt.empty:
            print(" No records to display.")
            return

        calories = self.listt["Calories"].sum()
        average = self.listt["Time (Minutes)"].mean()
        count = self.listt["Workout"].value_counts()

        print("\nProgress Report:")
        print(f"Total Calories Burned: {calories}")
        print(f"Average Session Time: {average:.2f} mins")
        print("\nWorkout Frequency:\n", count)

    def get_filtered_logs(self, workout=None, fdate=None, todate=None):
        logs = self.listt.copy()

        if workout:
            logs = logs[logs["Workout"].str.lower() == workout.lower()]
        if fdate:
            logs = logs[logs["Date"] >= fdate]
        if todate:
            logs = logs[logs["Date"] <= todate]
        return logs

    def plot_statistics(self):
        if self.listt.empty:
            print(" No workout data to display.")
            return
       
        self.listt["Date"] = pd.to_datetime(self.listt["Date"], errors='coerce')
        self.listt = self.listt.sort_values("Date")

        plt.figure(figsize=(12, 8))

        # 1. Bar Chart
        plt.subplot(2, 2, 1)
        sns.barplot(x="Workout", y="Time (Minutes)", data=self.listt, estimator=sum, ci=None, palette="Set1")
        plt.title("Total Time per Workout")
        plt.xlabel("Workout Type")
        plt.ylabel("Total Minutes")

        # 2. Line Chart 
        plt.subplot(2, 2, 2)
        daily_calories = self.listt.groupby("Date")["Calories"].sum()
        plt.plot(daily_calories.index, daily_calories.values, marker="o", color="orange", linewidth=2)
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories Burned")
        plt.grid(True)

        # 3. Pie Chart
        plt.subplot(2, 2, 3)
        counts = self.listt["Workout"].value_counts()
        plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%",
                startangle=90, colors=sns.color_palette("Set2"))
        plt.title("Workout Type Distribution")

        # 4. Heatmap
        plt.subplot(2, 2, 4)
        corr = self.listt[["Time (Minutes)", "Calories"]].corr()
        sns.heatmap(corr, annot=True, cmap="plasma", fmt=".2f")
        plt.title("Time vs Calories Correlation")

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    record= FitnessDashboard()

    while True:
        print("\n----- Health Tracking Menu -----")
        print("1. Add Workout Detail")
        print("2. View Report Detail ")
        print("3. Search Logs Detail")
        print("4. Show Graphs Detail")
        print("5. Exit \n")

        choice =int(input("Enter your choice : "))

        if choice == 1:
            type= input("Enter workout type (Running, Yoga, Cycling, etc.): ")
            try:
                duration= int(input("Enter duration (minutes): "))
                calories= int(input("Enter calories burned: "))
                record.add_entry(type, duration, calories)
            except ValueError:
                print(" Enter valid numbers for time and calories.")

        elif choice == 2:
            record.show_summary()

        elif choice == 3:
            filter=input("Filter by workout (press Enter to skip): ")
            start=input("Start date (YYYY-MM-DD) or Enter: ")
            end=input("End date (YYYY-MM-DD) or Enter: ")
            result= record.get_filtered_logs(filter if filter else None,
                                                start if start else None,
                                                end if end else None)
            print("\nFiltered Logs show here:\n", result)

        elif choice == 4:
            record.plot_statistics()

        elif choice == 5:
            print(" Exiting dashboard. Goodbye! \n")
            break

        else:
            print(" Invalid option. Try again.\n")
            break
