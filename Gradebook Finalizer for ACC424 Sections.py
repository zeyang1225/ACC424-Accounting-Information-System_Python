import pandas as pd

# === Step 1: Load CSV File ===
file_path = "your_filename.csv"  # Replace with actual file name
df = pd.read_csv(file_path)

# === Step 2: Identify Homework and Quiz Columns ===
homework_cols = [col for col in df.columns if col.startswith("Homework")]
quiz_cols = [col for col in df.columns if col.startswith("Quiz") and "Bonus" not in col]

# === Step 3: Replace Missing Values ===
df[homework_cols] = df[homework_cols].fillna(0)
df[quiz_cols] = df[quiz_cols].fillna(0)

# === Step 4: Calculate Top 10 Homework and Quiz Totals ===
df["Top10_Homework_Total"] = df[homework_cols].apply(lambda row: sum(sorted(row, reverse=True)[:10]), axis=1)
df["Top10_Quiz_Total"] = df[quiz_cols].apply(lambda row: sum(sorted(row, reverse=True)[:10]), axis=1)

# === Step 5: Extract Exam Scores ===
exam_cols = [
    "Midterm Exam 1 (12085265)",
    "Midterm Exam 2 (12107538)",
    "Final Exam (12117946)"
]
df[exam_cols] = df[exam_cols].fillna(0)
df["Midterm_1"] = df["Midterm Exam 1 (12085265)"]
df["Midterm_2"] = df["Midterm Exam 2 (12107538)"]
df["Final_Exam"] = df["Final Exam (12117946)"]

# === Step 6: Create Weighted Final Exam Score ===
df["Final_weighted"] = df["Final_Exam"] * 1.5

# === Step 7: Calculate Total Score ===
df["Total_Score"] = (
    df["Top10_Homework_Total"] +
    df["Top10_Quiz_Total"] +
    df["Midterm_1"] +
    df["Midterm_2"] +
    df["Final_weighted"]
)

# === Step 8: Calculate Grade Percentage ===
df["Grade_percent"] = df["Total_Score"] / 550 * 100

# === Step 9: Assign Letter Grades ===
def assign_letter_grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'E'

df["Grade"] = df["Grade_percent"].apply(assign_letter_grade)

# === Optional: Export Final Gradebook ===
# df.to_csv("Final_Grades_Section.csv", index=False)

# Preview Final Columns
print(df[["Student", "Top10_Homework_Total", "Top10_Quiz_Total", "Midterm_1", "Midterm_2", "Final_Exam", "Final_weighted", "Total_Score", "Grade_percent", "Grade"]].head())
