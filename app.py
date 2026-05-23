import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# ---------------- LOAD DATA ----------------
data = pd.read_csv("data.csv")
data.columns = data.columns.str.strip()

# Convert target
data["Do you procrastinate?"] = data["Do you procrastinate?"].map({
                                                                  "Yes": 1, "No": 0})

# Features
X = data[[
    "How many  do you study per day?",
    "How many  do you spend on your phone daily?",
    "How many  do you sleep daily?"
]]
y = data["Do you procrastinate?"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Dataset averages
avg_study = X.iloc[:, 0].mean()
avg_phone = X.iloc[:, 1].mean()
avg_sleep = X.iloc[:, 2].mean()

# ---------------- UI ----------------
st.set_page_config(page_title="Productivity Analyzer", layout="centered")

st.title("📊 Student Productivity & Behavior Analyzer")

st.markdown("Analyze your habits and get smart insights.")

# Inputs
study = st.slider("📚 Study Hours", 0, 10, 2)
phone = st.slider("📱 Phone Usage", 0, 10, 5)
sleep = st.slider("😴 Sleep Hours", 0, 10, 6)

# ---------------- FUNCTIONS ----------------


def risk_score(study, phone, sleep):
    score = (phone * 12) - (study * 8) - (sleep * 4)
    return max(0, min(100, score))


def profile(score):
    if score > 70:
        return "🔴 High-Risk Procrastinator"
    elif score > 40:
        return "🟠 Distracted Learner"
    elif score > 20:
        return "🟢 Balanced Student"
    else:
        return "🔵 Highly Disciplined"


# ---------------- BUTTON ----------------
if st.button("Analyze Now"):

    # Prediction
    input_data = pd.DataFrame([[study, phone, sleep]], columns=X.columns)
    pred = model.predict(input_data)[0]

    # Score
    score = risk_score(study, phone, sleep)
    productivity = 100 - score

    # Result
    st.subheader("🔍 Result")
    st.write("Procrastination Status:", "Yes" if pred == 1 else "No")

    # Score
    st.subheader("📈 Productivity Index")
    st.progress(productivity/100)
    st.write(f"{productivity:.1f} / 100")

    # Profile
    st.subheader("👤 Behavior Profile")
    st.write(profile(score))

    # Comparison
    st.subheader("📊 Your Data vs Average")

    st.write(f"Study Hours: {study} (Avg: {avg_study:.1f})")
    st.write(f"Phone Usage: {phone} (Avg: {avg_phone:.1f})")
    st.write(f"Sleep Hours: {sleep} (Avg: {avg_sleep:.1f})")

    # Chart
    fig, ax = plt.subplots()
    labels = ["Study", "Phone", "Sleep"]
    user_values = [study, phone, sleep]
    avg_values = [avg_study, avg_phone, avg_sleep]

    ax.plot(labels, user_values, marker='o', label="You")
    ax.plot(labels, avg_values, marker='o', linestyle='--', label="Average")

    ax.set_title("Your Habits vs Average")
    ax.legend()

    st.pyplot(fig)

    # Insights
    st.subheader("💡 Smart Insights")

    if phone > avg_phone:
        st.write("• Your phone usage is higher than average")
    if study < avg_study:
        st.write("• Your study time is below average")
    if sleep < avg_sleep:
        st.write("• Your sleep may be insufficient")

    # Suggestions
    st.subheader("📌 Recommendations")

shown = False

if phone > 5:
    st.write("• Reduce phone usage")
    shown = True

if study < 3:
    st.write("• Increase study time")
    shown = True

if sleep < 6:
    st.write("• Maintain better sleep schedule")
    shown = True

if not shown:
    st.write("✅ Your habits look good! Keep it up.")
