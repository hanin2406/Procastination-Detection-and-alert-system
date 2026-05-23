import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Clean column names (important)
data.columns = data.columns.str.strip()

# Calculate average values
avg_phone = data["How many  do you spend on your phone daily?"].mean()
avg_study = data["How many  do you study per day?"].mean()
avg_sleep = data["How many  do you sleep daily?"].mean()

# Labels and values
labels = ["Phone Usage", "Study Time", "Sleep Time"]
values = [avg_phone, avg_study, avg_sleep]

# Create line plot
plt.figure(figsize=(8, 5))
plt.plot(labels, values, marker='o', linewidth=3)

# Titles and labels
plt.title("Average Time Comparison (Phone vs Study vs Sleep)")
plt.xlabel("Activities")
plt.ylabel("Hours")

# Grid
plt.grid(True)

# Save graph
plt.savefig("line_plot.png")

# Show graph
plt.show()


# Load dataset
data = pd.read_csv("data.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Set style
sns.set(style="whitegrid")

# Create count plot
sns.countplot(x="Do you procrastinate?", data=data)

# Title and labels
plt.title("Procrastination Distribution")
plt.xlabel("Do you procrastinate?")
plt.ylabel("Number of Students")

# Show chart
plt.show()
