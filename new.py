# ==========================================
# WEATHER DATA ANALYSIS PROJECT
# Using Pandas, Seaborn, Matplotlib only
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# STEP 1: LOAD DATASET
# ---------------------------
df = pd.read_csv("weather.csv")   # <- Tamaro dataset (250k+ rows)

print("Original Dataset Shape:", df.shape)

# ---------------------------
# STEP 2: DATA CLEANING
# ---------------------------

# Check for missing values
print("\nMissing Values Before Cleaning:\n", df.isnull().sum())

# Fill missing values with column mean
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].mean())
df['WindSpeed'] = df['WindSpeed'].fillna(df['WindSpeed'].mean())

# Remove duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:", df.shape)

# ---------------------------
# STEP 3: VISUALIZATION
# ---------------------------

# 1. Line Plot – Temperature trend per city
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="Year", y="Temperature", hue="City", marker="o")
plt.title("Yearly Temperature Trend per City")
plt.show()

# 2. Bar Chart – Average Rainfall per City
plt.figure(figsize=(8,6))
sns.barplot(data=df, x="City", y="Rainfall", ci=None, palette="Set2")
plt.title("Average Rainfall by City")
plt.show()

# 3. Scatter Plot – Temperature vs Humidity
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Temperature", y="Humidity", hue="City", alpha=0.7)
plt.title("Temperature vs Humidity")
plt.show()

# 4. Histogram – Wind Speed Distribution
plt.figure(figsize=(8,6))
sns.histplot(df["WindSpeed"], bins=15, kde=True, color="orange")
plt.title("Distribution of Wind Speed")
plt.show()

# 5. Heatmap – Correlation Matrix
plt.figure(figsize=(8,6))
sns.heatmap(df[["Temperature","Rainfall","Humidity","WindSpeed"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ---------------------------
# STEP 4: FINAL SUMMARY
# ---------------------------

print("\n===== FINAL SUMMARY REPORT =====")
print("Total Records:", len(df))
print("Average Temperature (°C):", round(df["Temperature"].mean(),2))
print("Average Rainfall (mm):", round(df["Rainfall"].mean(),2))
print("Average Humidity (%):", round(df["Humidity"].mean(),2))
print("Average Wind Speed (km/h):", round(df["WindSpeed"].mean(),2))

print("\nHottest City (Avg Temp):", df.groupby("City")["Temperature"].mean().idxmax())
print("Wettest City (Avg Rainfall):", df.groupby("City")["Rainfall"].mean().idxmax())
print("Year with Highest Avg Temperature:", df.groupby("Year")["Temperature"].mean().idxmax())
print("Year with Most Rainfall:", df.groupby("Year")["Rainfall"].mean().idxmax())