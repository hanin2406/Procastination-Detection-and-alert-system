import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

# Convert target
data["Do you procrastinate?"] = data["Do you procrastinate?"].map({
                                                                  "Yes": 1, "No": 0})

# Features (use your column names)
X = data[[
    "How many  do you study per day?",
    "How many  do you spend on your phone daily?",
    "How many  do you sleep daily?"
]]

y = data["Do you procrastinate?"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Model ready!")

# Test input
study = float(input("Study hours: "))
phone = float(input("Phone usage: "))
sleep = float(input("Sleep hours: "))

result = model.predict([[study, phone, sleep]])

if result[0] == 1:
    print("Procrastinator")
else:
    print("Not a Procrastinator")
