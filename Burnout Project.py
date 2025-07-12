import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data_file = pd.read_csv("mental_health_workplace_survey.csv")

# print(data_file.shape)
print(data_file.columns)
# print(data_file.head())
print(data_file.info())
# print(data_file.describe())

#nulines reiksmes
# print(data_file.isnull().sum())

# duplikatai
# print(data_file.duplicated().sum())

print("----------------------------------------------------------------")
print("How does the number of hours employees work per week relate to their burnout level, and how does this link to burnout risk?")
print()
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data_file, x='WorkHoursPerWeek', y='BurnoutLevel', hue='BurnoutRisk')
plt.title("Burnout Level vs Work Hours per Week")
plt.xlabel("Work Hours per Week")
plt.ylabel("Burnout Level")
plt.tight_layout()
plt.show()
print()
print("Conclusions: While burnout level directly relates to burnout risk, work hours alone do not explain burnout. Other factors (like stress, sleep, manager support, etc.) may be more influential. ")
print()
print()
print("----------------------------------------------------------------")
print("How does burnout level vary across different departments?")
print()
plt.figure(figsize=(10, 6))
sns.boxplot(data=data_file, x='Department', y='BurnoutLevel')
plt.title("Burnout Level by Department")
plt.xlabel("Department")
plt.ylabel("Burnout Level")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Burnout affects employees across all departments similarly. There’s no department with clearly higher or lower burnout, suggesting other factors (e.g., job role, workload, manager support) may play a more important role than department itself.")
print()
print()
print("----------------------------------------------------------------")
print("Is there a relationship between how much employees sleep and their productivity, and how does burnout risk affect that relationship?")
print()
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data_file, x='SleepHours', y='ProductivityScore', hue='BurnoutRisk')
plt.title("Sleep Hours vs Productivity Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")
plt.tight_layout()
plt.show()
print()
print("Conclusions: There is no strong visible relationship between sleep hours and productivity. However, burnout risk appears to correlate with lower productivity, regardless of how much sleep someone gets.")
print()
print("----------------------------------------------------------------")
print("Which job roles report higher burnout?")
print()
plt.figure(figsize=(8, 6))
sns.boxplot(data=data_file, x='JobRole', y='BurnoutLevel', hue='BurnoutRisk')
plt.title("Job Role vs Burnout Level")
plt.xlabel("Job Role")
plt.ylabel("Burnout Level")
sns.despine(offset=10, trim=True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Burnout level is a strong, reliable indicator of burnout risk across all roles. No job role appears to have uniquely high or low burnout patterns — burnout affects many roles equally. This suggests that organizational culture or personal factors (not just role type) may drive burnout.")
print()
print("----------------------------------------------------------------")
print("Are people with mental health support less burned out?")
print()
plt.figure(figsize=(8, 6))
sns.boxplot(data=data_file, x='HasMentalHealthSupport', y='BurnoutLevel', hue='BurnoutRisk')
plt.title("Has Mental Health Support vs Burnout Level")
plt.xlabel("Has Mental Health Support")
plt.ylabel("Burnout Level")
sns.despine(offset=10, trim=True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Mental health support does not significantly lower burnout levels for high-risk individuals — likely because support may come too late, or it’s not effective enough on its own. For low-risk employees, the difference is small but slightly better when support is available.")
print()
print("----------------------------------------------------------------")
print("How does burnout risk vary across different gender groups?")
print()
filtered_gender = data_file[data_file['Gender'] != 'Non-binary']
filtered_gender2 = filtered_gender[filtered_gender['Gender'] != 'Prefer not to say']
sns.relplot(data=filtered_gender2, x='WorkHoursPerWeek', y='BurnoutLevel', hue='Gender')
plt.show()
plt.figure(figsize=(6, 5))
sns.countplot(data=data_file, x='Gender', hue='BurnoutRisk')
plt.title("Burnout Risk by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Burnout risk appears to be present in similar proportions across all gender identities and required further analysis.")
print()
print("----------------------------------------------------------------")
print("How does the average burnout level vary based on how long employees have been with the company?")
print()
data_file['NEWYearsAtCompanyGroup'] = pd.cut(data_file['YearsAtCompany'], bins=[0, 2, 5, 10, 20], labels=['0-2', '2-5', '5-10', '10+'])
plt.figure(figsize=(8, 6))
sns.barplot(data=data_file, x='NEWYearsAtCompanyGroup', y='BurnoutLevel')
plt.title("Years At Company vs Burnout Level")
plt.xlabel("Years At Company")
plt.ylabel("Burnout Level")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Average burnout levels are stable across different time period groups, indicating that years at the company does not strongly influence burnout on its own.")
print()
print("----------------------------------------------------------------")
print("How does an employee’s work-life balance rating relate to their risk of burnout?")
print()
print(data_file['WorkLifeBalanceScore'])
print(max(data_file['WorkLifeBalanceScore']))
print(min(data_file['WorkLifeBalanceScore']))
def work_life_balance_categorization(score):
        if score <= 2:
                return "Poor"
        if score <= 4:
                return "Below Average"
        if score <= 6:
                return "Average"
        if score <= 8:
                return "Good"
        else:
                return "Excellent"
data_file['NEW_W_L_Balance']= data_file['WorkLifeBalanceScore'].apply(work_life_balance_categorization)
plt.figure(figsize=(8, 6))
sns.countplot(data=data_file, x='NEW_W_L_Balance',hue='BurnoutRisk')
plt.title("Work Life Balance vs Burnout Level")
plt.xlabel("Work Life Balance Rating")
plt.ylabel("Employee Number")
plt.tight_layout()
plt.show()
print()
print("Conclusions: There’s a strong relationship between work-life balance and burnout risk.")
print("Employees with poor balance are much more likely to be at high risk of burnout.")
print("Improving perceived work-life balance could be a key preventive measure in managing employee burnout.")
print()
print("----------------------------------------------------------------")
print("How does the level of perceived manager support relate to employee burnout risk?")
print()
print("Manager support score")
print(data_file['ManagerSupportScore'])
print(max(data_file['ManagerSupportScore']))  #9.99
print(min(data_file['ManagerSupportScore']))  #1.0
def manager_support(score):
        if score <= 2:
                return "No support"
        if score <= 4:
                return "Weak support"
        if score <= 6:
                return "Mixed support"
        if score <= 8:
                return "Solid support"
        else:
                return "Reliable support"
data_file['NEW_ManagerSupport']= data_file['ManagerSupportScore'].apply(manager_support)
order = ["No support", "Weak support", "Mixed support", "Solid support", "Reliable support"]
data_file['NEW_ManagerSupport'] = pd.Categorical(
    data_file['NEW_ManagerSupport'],
    categories=order,
    ordered=True
)
plt.figure(figsize=(8, 6))
sns.countplot(data=data_file, x='NEW_ManagerSupport', hue='BurnoutRisk')
plt.title("Manager Support vs Burnout Risk")
plt.xlabel("Manager Support Score")
plt.ylabel("Employees No.")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Employees who perceive reliable or solid support from managers are far less likely to experience burnout.")
print()
print("----------------------------------------------------------------")
print("How does the level of physical activity relate to employee burnout risk?")
print()
print("Physical activity hrs")
print(data_file['PhysicalActivityHrs'])
print(max(data_file['PhysicalActivityHrs']))  #10.0
print(min(data_file['PhysicalActivityHrs']))  #0.0
def physical_activity(score):
    if score ==0:
        return "None"
    if score <=2:
        return "Minimal effort"
    if score <= 4:
        return "Some physical activity"
    if score <= 7:
        return "Recommended level"
    if score <= 9:
        return "Active lifestyle"
    else:
        return "Athletic-focused"
data_file['NEW_PhysicalActivity'] = data_file['PhysicalActivityHrs'].apply(physical_activity)
order_activity = ["None", "Minimal effort", "Some physical activity", "Recommended level", "Active lifestyle", "Athletic-focused"]
data_file['NEW_PhysicalActivity'] = pd.Categorical(
    data_file['NEW_PhysicalActivity'],
    categories=order_activity,
    ordered=True
)
plt.figure(figsize=(8, 6))
sns.countplot(data=data_file, x='NEW_PhysicalActivity', hue='BurnoutRisk')
plt.title("Physical Activity vs Burnout Risk")
plt.xlabel("Physical Activity Rate")
plt.ylabel("Employees No.")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Moderate physical activity (4–7 hours/week) is the most common and is associated with lower burnout risk.")
print("Minimal activity (0–2 hours) appears to correlate with a higher risk of burnout.")
print("High levels of activity (7+ hours) may also be linked to lower burnout, but fewer people fall in that category.")
print()
print("----------------------------------------------------------------")
print("Does the perception of career growth opportunities affect employee burnout risk?")
print()
print("Career growth score")
print(data_file['CareerGrowthScore'])
print(max(data_file['CareerGrowthScore']))  #9.99
print(min(data_file['CareerGrowthScore']))  #1.0
def career_growth(score):
    if score <=2:
        return "Stagnant"
    if score <= 4:
        return "Limited Growth"
    if score <= 6:
        return "Moderate Growth"
    if score <= 8:
        return "Strong Growth"
    else:
        return "Excellent Growth"
data_file['NEW_CareerGrowth'] = data_file['CareerGrowthScore'].apply(career_growth)
order_career = ["Stagnant", "Limited Growth", "Moderate Growth", "Strong Growth", "Excellent Growth"]
data_file['NEW_CareerGrowth'] = pd.Categorical(
    data_file['NEW_CareerGrowth'],
    categories=order_career,
    ordered=True
)
plt.figure(figsize=(8, 6))
sns.countplot(data=data_file, x='NEW_CareerGrowth', hue='BurnoutRisk')
plt.title("Career Growth vs Burnout Risk")
plt.xlabel("Career Growth Rate")
plt.ylabel("Employees No.")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: There is a clear trend: better perceived career growth is associated with lower burnout risk.")
print("Companies should invest in employee development, promotions, and growth paths to reduce burnout levels.")
print()
print("----------------------------------------------------------------")
print("How does salary range relate to employee productivity levels?")
print()
print("Salary") #already has ranges
print(data_file['SalaryRange'])
print(max(data_file['SalaryRange']))
print(min(data_file['SalaryRange']))
print(max(data_file['ProductivityScore']))
print(min(data_file['ProductivityScore']))
def productivity(score):
    if score <=2.5:
        return "Very low"
    if score <= 5:
        return "Low"
    if score <= 7:
        return "Average"
    if score <= 8.5:
        return "High"
    else:
        return "Very high"
data_file['NEW_Productivity'] = data_file['ProductivityScore'].apply(productivity)
order_productivity = ["Very low", "Low", "Average", "High", "Very high"]
data_file['NEW_Productivity'] = pd.Categorical(
    data_file['NEW_Productivity'],
    categories=order_productivity,
    ordered=True
)
plt.figure(figsize=(8, 6))
sns.countplot(data=data_file, x='SalaryRange', hue='NEW_Productivity')
plt.title("Salary Range vs Productivity")
plt.xlabel("Salary Range")
plt.ylabel("Employees No.")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: There is a clear trend: better perceived career growth is associated with lower burnout risk.")
print("Companies should invest in employee development, promotions, and growth paths to reduce burnout levels.")
print()
print("----------------------------------------------------------------")
print("How does work-life balance affect productivity under different working hour conditions?")
print()
g = sns.catplot(
    data=data_file,
    x='NEW_W_L_Balance',
    y='ProductivityScore',
    col='SalaryRange',
    kind='box',
    col_wrap=3,
    height=4,
    aspect=1
)
g.set_titles("Salary Range: {col_name}")
g.set_xticklabels(rotation=30)
plt.tight_layout()
plt.show()

def working_hours(score):
    if score <=35:
        return "Part-time"
    if score <= 40:
        return "Standard"
    if score <= 45:
        return "Slightly extended"
    if score <= 50:
        return "Heavy"
    else:
        return "Excessive"
data_file['NEW_WorkingHours'] = data_file['WorkHoursPerWeek'].apply(working_hours)
order_working_h = ["Part-time", "Standard", "Slightly extended", "Heavy", "Excessive"]
data_file['NEW_WorkingHours'] = pd.Categorical(
    data_file['NEW_WorkingHours'],
    categories=order_working_h,
    ordered=True
)
group = sns.catplot(
    data=data_file,
    x='NEW_W_L_Balance',
    y='ProductivityScore',
    col='NEW_WorkingHours',
    kind='box',
    col_wrap=3,
    height=4,
    aspect=1
)
group.set_titles("Working Hours Rate: {col_name}")
group.set_xticklabels(rotation=30)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Good work-life balance helps maintain productivity, especially when work hours increase.")
print("Poor work-life balance with excessive hours appears risky, possibly leading to burnout and reduced productivity")
print("This graph provides a multi-factor insight, showing that work-life balance is not universally equal in impact—it interacts with work hour load.")
print()
print("----------------------------------------------------------------")
print("Does commute time influence employee burnout levels?")
print()
plt.figure(figsize=(8, 6))
sns.lineplot(data=data_file, x='CommuteTime', y='BurnoutLevel')
plt.title("Commute Time vs Burnout Level")
plt.xlabel("Commute Time (Minutes)")
plt.ylabel("Burnout Level")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Commute time does not show a consistent impact on burnout level based on this data.")
print()
print("---------------MALE EMPLOYEES------------------------------------")
print()
print("----------------------------------------------------------------")
print("How does sleep duration relate to burnout level, and how does job satisfaction interact with this?")
man = data_file[data_file['Gender'] == 'Male']
woman = data_file[data_file['Gender'] == 'Female']
plt.figure(figsize=(8, 6))
sns.scatterplot(data=man, x='SleepHours', y='BurnoutLevel', hue='JobSatisfaction')
plt.title("Sleep Hours vs Burnout Level")
plt.xlabel("Sleep Hours")
plt.ylabel("Burnout Level")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Job satisfaction moderates burnout risk more clearly than sleep duration.")
print("Sleep hours alone are not a reliable burnout predictor — individuals with sufficient sleep still report burnout if satisfaction is low.")
print("For male employees, improving job satisfaction may be more effective than adjusting sleep patterns in reducing burnout.")
print()
print("----------------------------------------------------------------")
print("How does burnout level vary across different job roles and burnout risk categories?")
plt.figure(figsize=(8, 6))
sns.boxplot(data=man, x='JobRole', y='BurnoutLevel', hue='BurnoutRisk')
plt.title("Job Role vs Burnout Level")
plt.xlabel("Job Role")
plt.ylabel("Burnout Level")
sns.despine(offset=10, trim=True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Job role has a noticeable effect on burnout level.")
print("Some roles, especially Project Managers and HR, may warrant additional wellness or support resources.")
print()
print()
print("---------------FEMALE EMPLOYEES------------------------------------")
print()
print("----------------------------------------------------------------")
print("How does sleep duration relate to burnout level, and how does job satisfaction interact with this?")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=woman, x='SleepHours', y='BurnoutLevel', hue='JobSatisfaction')
plt.title("Sleep Hours vs Burnout Level")
plt.xlabel("Sleep Hours")
plt.ylabel("Burnout Level")
plt.tight_layout()
plt.show()
print()
print("Conclusions: Job satisfaction moderates burnout risk more clearly than sleep duration.")
print("Female group shows a slightly wider vertical spread in burnout levels at each sleep hour, suggesting greater variance in burnout for the same sleep duration.")
print()
print("----------------------------------------------------------------")
print("How does burnout level vary across different job roles and burnout risk categories?")
plt.figure(figsize=(8, 6))
sns.boxplot(data=woman, x='JobRole', y='BurnoutLevel', hue='BurnoutRisk')
plt.title("Job Role vs Burnout Level")
plt.xlabel("Job Role")
plt.ylabel("Burnout Level")
sns.despine(offset=10, trim=True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
print()
print("Conclusions: Job role significantly influences burnout among women.")
print("Some roles (e.g., HR, Project Management) may demand targeted interventions.")
print()
print("----------------------------------------------------------------")



