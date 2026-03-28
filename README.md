EXAM SCORE PRETICTOR

Academic performance is influenced by multiple behavioral, psychological, and environmental factors. However, understanding which factors matter most is often unclear.
This project, Exam Score Predictor, aims to perform data-driven analysis to answer:
“How do student lifestyle habits impact exam performance?”

🎯 Project Goals
Perform data cleaning & preprocessing
Conduct Exploratory Data Analysis (EDA)
Identify key performance drivers
Build a foundation for predictive modeling
Generate actionable insights


🧩 Dataset Overview
📦 Total Records: 1000 students
📊 Features: 16 columns
🎯 Target Variable: exam_score
🔍 Data Schema

Type	Columns
Numerical	age, study_hours_per_day, social_media_hours, netflix_hours, attendance_percentage, sleep_hours, exercise_frequency, mental_health_rating, exam_score
Categorical	gender, part_time_job, diet_quality, parental_education_level, internet_quality, extracurricular_participation
Identifier	student_id


🔬 Data Preprocessing Pipeline
✅ 1. Data Loading
df = pd.read_csv("student_habits_performance.csv")
✅ 2. Data Inspection
Checked structure, null values, and datatypes
Dataset size: (1000, 16)
✅ 3. Handling Missing Values
Total missing values: 91
df.dropna(inplace=True)

📌 Result:

Clean dataset: 909 rows
✅ 4. Duplicate Handling
df.duplicated().sum()

✔ No duplicate records found

✅ 5. Feature Categorization
categorical_cols = [
    "gender", "part_time_job", "diet_quality",
    "parental_education_level", "internet_quality",
    "extracurricular_participation"
]
📊 Exploratory Data Analysis (EDA)
🔢 Statistical Summary
df.describe()
📈 Key Metrics
Avg Exam Score: 69.55
Avg Study Hours: 3.53 hrs/day
Avg Sleep: 6.47 hrs
Avg Mental Health: 5.46 / 10
📌 Categorical Insights
Feature	Insight
Gender	Balanced distribution
Diet	Majority have "Fair" or "Good"
Job	Most students do NOT work part-time
Internet	Mostly Good/Average
📈 Behavioral Insights
📚 Study vs Score

✔ Strong positive correlation
➡ Students studying >5 hours perform better

📱 Social Media Impact

❌ Higher usage → lower exam scores

😴 Sleep Effect

⚖ Optimal sleep (6–8 hrs) → better performance

🧠 Mental Health

✔ Higher ratings → higher scores

🏫 Attendance

🔥 One of the strongest predictors of success

📉 Visualization Strategy
📦 Libraries Used
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
📊 Plots Created
Distribution plots (histograms)
Count plots (categorical features)
Box plots (outlier detection)
Correlation heatmap
🔗 Feature Relationships (Conceptual)
Feature	Relationship with Exam Score
study_hours	⬆ Positive
attendance	⬆ Strong Positive
social_media	⬇ Negative
netflix_hours	⬇ Negative
sleep_hours	⚖ Optimal Range
mental_health	⬆ Positive
🧠 Key Findings
🔥 High Impact Factors
Study hours
Attendance
Mental health
⚠️ Negative Factors
Social media overuse
Excess entertainment time
⚖️ Balanced Factors
Sleep (too low or too high is harmful)
Exercise (moderate benefit)
🏗️ Project Architecture
📁 Exam-Score-Predictor
│
├── 📄 notebook.ipynb / notebook.py
├── 📄 student_habits_performance.csv
├── 📄 README.md
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/exam-score-predictor.git
cd exam-score-predictor
2️⃣ Install Dependencies
pip install -r requirements.txt
Example requirements.txt:
pandas
numpy
matplotlib
seaborn
jupyter
▶️ Usage
jupyter notebook

Run all cells step-by-step:

Data Loading
Data Cleaning
EDA
Visualization
📦 Future Enhancements
🔮 Machine Learning Integration
Linear Regression
Random Forest
XGBoost
🎯 Prediction Goal
exam_score = f(student habits)
🌐 Deployment Ideas
Streamlit dashboard
Flask web app
Interactive analytics dashboard
📊 Potential Research Extensions
Feature importance analysis
Clustering student behavior patterns
Recommendation system
⚠️ Limitations
Dataset is limited
Missing values removed (data loss)
No time-series analysis
Correlation ≠ causation
🤝 Contribution Guidelines
Fork the repo
Create a branch
Commit changes
Submit pull request
📜 License

MIT License – free to use and modify

👨‍💻 Author

Hassan (Mohi)
🎯 Python Developer | Machine Learning Enthusiast
