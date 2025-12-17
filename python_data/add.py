import pandas as pd

# Load dataset provided by user
df = pd.read_csv("fitness_activities_100rows.csv")

class FitnessTracker:
    def __init__(self, data):
        self.data = data

    def log_activity(self, activity_type, duration, calories):
        if duration <= 0:
            print("Duration must be positive!")
            return
        if calories <= 0:
            print("Calories must be positive!")
            return

        new_entry = {
            "date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "activity_type": activity_type,
            "duration_minutes": duration,
            "calories_burned": calories
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_entry])], ignore_index=True)
        print("Activity logged successfully!")

    def calculate_metrics(self):
        total_calories = self.data["calories_burned"].sum()
        avg_duration = self.data["duration_minutes"].mean()
        freq = self.data["activity_type"].value_counts()

        return total_calories, avg_duration, freq

    def filter_activities(self, condition):
        if isinstance(condition, str):
            return self.data[self.data["activity_type"] == condition]
        if isinstance(condition, tuple) and len(condition) == 2:
            start, end = condition
            return self.data[(self.data["date"] >= start) & (self.data["date"] <= end)]
        return None

    def generate_report(self):
        total_cal, avg_dur, freq = self.calculate_metrics()
        print("\n===== FITNESS REPORT =====")
        print("Total Calories Burned:", total_cal)
        print("Average Duration:", round(avg_dur, 2), "minutes")
        print("\nActivity Frequency:\n", freq)
        print("==========================\n")


tracker = FitnessTracker(df)

print("Enter your activity:")
atype = input("Activity Type: ")
dur = int(input("Duration (minutes): "))
cal = int(input("Calories Burned: "))

tracker.log_activity(atype, dur, cal)

tracker.generate_report()

print("\nFiltered by 'Running':")
print(tracker.filter_activities("Running"))

print("\nFiltered by Date Range (2025-01-05 to 2025-01-20):")
print(tracker.filter_activities(("2025-01-05", "2025-01-20")))













import pandas as pd
import numpy as np

# Load dataset provided by user
df = pd.read_csv("fitness_activities_100rows.csv")

class FitnessTracker:
    def __init__(self, data):
        self.data = data
        self.clean_data()

    # -------------------------------
    # CLEAN DATA USING PANDAS
    # -------------------------------
    def clean_data(self):
        self.data = self.data.dropna()
        self.data = self.data[(self.data["duration_minutes"] > 0) &
                              (self.data["calories_burned"] > 0)]
        self.data["date"] = pd.to_datetime(self.data["date"])
        print("Data cleaned successfully!")

    # -------------------------------
    # LOG ACTIVITY WITH VALIDATION
    # -------------------------------
    def log_activity(self, activity_type, duration, calories):
        if duration <= 0:
            print("Duration must be positive!")
            return
        if calories <= 0:
            print("Calories must be positive!")
            return

        new_entry = {
            "date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "activity_type": activity_type,
            "duration_minutes": duration,
            "calories_burned": calories
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_entry])], ignore_index=True)
        print("Activity logged successfully!")

    # -------------------------------
    # BASIC METRICS
    # -------------------------------
    def calculate_metrics(self):
        total_calories = self.data["calories_burned"].sum()
        avg_duration = self.data["duration_minutes"].mean()
        freq = self.data["activity_type"].value_counts()
        return total_calories, avg_duration, freq

    # -------------------------------
    # FILTER ACTIVITIES
    # -------------------------------
    def filter_activities(self, condition):
        if isinstance(condition, str):
            return self.data[self.data["activity_type"] == condition]

        if isinstance(condition, tuple) and len(condition) == 2:
            start, end = condition
            return self.data[(self.data["date"] >= start) & (self.data["date"] <= end)]

        return None

    # -------------------------------
    # ADVANCED ANALYSIS (NUMPY + PANDAS)
    # -------------------------------
    def advanced_analysis(self):
        print("\n=== ADVANCED DATA ANALYSIS ===")

        # NUMPY: averages
        avg_duration = np.mean(self.data["duration_minutes"])
        avg_calories = np.mean(self.data["calories_burned"])

        # NUMPY: percentage improvement
        first_10 = self.data.head(10)["calories_burned"].mean()
        last_10 = self.data.tail(10)["calories_burned"].mean()
        percent_improve = ((last_10 - first_10) / first_10) * 100 if first_10 != 0 else 0

        # PANDAS: group by activity
        group_activity = self.data.groupby("activity_type").agg({
            "duration_minutes": "sum",
            "calories_burned": "sum"
        })

        # PANDAS: weekly trends
        self.data["week"] = self.data["date"].dt.isocalendar().week
        weekly = self.data.groupby("week").agg({
            "duration_minutes": "sum",
            "calories_burned": "sum"
        })

        # Total time spent per activity
        time_per_activity = self.data.groupby("activity_type")["duration_minutes"].sum()

        print("Daily Average Duration:", avg_duration)
        print("Daily Average Calories:", avg_calories)
        print("Percentage Improvement (First 10 vs Last 10):", percent_improve)
        print("\nGroup by Activity Type:\n", group_activity)
        print("\nWeekly Trends:\n", weekly)
        print("\nTotal Time Per Activity Type:\n", time_per_activity)

    # -------------------------------
    # REPORT
    # -------------------------------
    def generate_report(self):
        total_cal, avg_dur, freq = self.calculate_metrics()

        print("\n===== FITNESS REPORT =====")
        print("Total Calories Burned:", total_cal)
        print("Average Duration:", round(avg_dur, 2), "minutes")
        print("\nActivity Frequency:\n", freq)
        print("==========================")

        # Call advanced report inside final report
        self.advanced_analysis()


# -------------------------------
# RUN PROGRAM
# -------------------------------
tracker = FitnessTracker(df)

print("\nEnter your activity:")
atype = input("Activity Type: ")
dur = int(input("Duration (minutes): "))
cal = int(input("Calories Burned: "))

tracker.log_activity(atype, dur, cal)

tracker.generate_report()

print("\nFiltered by 'Running':")
print(tracker.filter_activities("Running"))

print("\nFiltered by Date Range (2025-01-05 to 2025-01-20):")
print(tracker.filter_activities(("2025-01-05", "2025-01-20")))



# Python gives built-in platforms like Shell and IDLE for writing and running code.

# When you install Python, Shell and IDLE are installed automatically along with it.


 






