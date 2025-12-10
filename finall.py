import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("fitness_activities_100rows.csv")


class FitnessTracker:
    def __init__(self, dataframe):
        self.data = dataframe

    def log_activity(self, activity_type, duration, calories):
        
        if duration <= 0 or calories <= 0:
            raise ValueError("Duration and Calories must be positive numbers.")

        new_row = {
            "date": pd.Timestamp.now().date(),
            "activity": activity_type,
            "duration_minutes": duration,
            "calories_burned": calories
        }

        self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)

    def calculate_metrics(self):
        total_calories = self.data["calories_burned"].sum()
        average_duration = self.data["duration_minutes"].mean()
        activity_frequency = self.data["activity"].value_counts()

        return total_calories, average_duration, activity_frequency

    def filter_activities(self, condition):
        return self.data.query(condition)

    def generate_report(self):
        total, avg, freq = self.calculate_metrics()
        return {
            "Total Calories Burned": total,
            "Average Duration": avg,
            "Activity Frequency": freq.to_dict()
        }


tracker = FitnessTracker(df)


tracker.log_activity("Running", 45, 350)
tracker.log_activity("Walking", 30, 150)


report = tracker.generate_report()
print("\n=== FITNESS REPORT ===")
print(report)


daily_avg_calories = np.mean(tracker.data["calories_burned"])
print("\nDaily Average Calories:", daily_avg_calories)

percentage_improvement = (
    (tracker.data["duration_minutes"].iloc[-1] - tracker.data["duration_minutes"].mean()) /
    tracker.data["duration_minutes"].mean()
) * 100

print("Percentage Duration Improvement:", percentage_improvement)

# -------------------------
# VISUALIZATIONS
# -------------------------

# 1 BAR CHART – Total duration per activity
plt.figure()
tracker.data.groupby("activity")["duration_minutes"].sum().plot(kind="bar")
plt.title("Total Time Spent per Activity")
plt.xlabel("Activity Type")
plt.ylabel("Total Minutes")
plt.tight_layout()
plt.show()

# 2 LINE CHART – Calories over time
plt.figure()
tracker.data.groupby("date")["calories_burned"].sum().plot(kind="line")
plt.title("Calories Burned Over Time")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.tight_layout()
plt.show()

# 3 PIE CHART – Activity distribution
plt.figure()
tracker.data["activity"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Activity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 4 HEATMAP – Correlation using matplotlib
plt.figure()
corr = tracker.data[["duration_minutes", "calories_burned"]].corr()
plt.imshow(corr, cmap="viridis", interpolation="nearest")
plt.colorbar()
plt.xticks([0, 1], ["Duration", "Calories"])
plt.yticks([0, 1], ["Duration", "Calories"])
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()