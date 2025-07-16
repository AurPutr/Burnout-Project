# Employee Burnout Analysis
## Project: Mental Health & Productivity Trends in the Workplace


## Description
This project aimed to explore the key factors influencing employee burnout using a real-world survey dataset. The objective was to uncover patterns between variables such as working hours, sleep, job role, manager support, and burnout risk — and to visualize these insights to guide employee well-being strategies.


## Project Overview
Using Python and popular data analysis libraries, the project walks through:
    - Cleaning and preparing a workplace mental health survey dataset
    - Visualizing burnout patterns using scatter plots, box plots, and categorical plots
    - Analyzing the impact of:
        - Work hours on burnout level
        - Sleep, job satisfaction, and productivity
        - Gender differences in burnout risk
        - Work-life balance, physical activity, and career growth perception
The project also includes **segmented analysis by gender and job role** to highlight how different groups experience burnout.


## Technologies Used
- **Python**
- **Pandas** – for data cleaning and manipulation
- **Seaborn / Matplotlib** – for visual analytics
- **Categorical binning** – to group continuous scores into qualitative categories for easier comparison


## Install
This project requires Python and the following packages:

 **pandas**
 **matplotlib**
 **seaborn**
Install them via pip:

```bash
    pip install pandas matplotlib seaborn
```

## Code
All analysis is implemented in a single Python file (e.g., `burnout_analysis.py`) and assumes the dataset `file mental_health_workplace_survey.csv` is in the same directory.


## Run
To run the script, simply execute:

    `python burnout_analysis.py`

This will open and display a series of plots in your default Python environment.


## Data
The dataset contains real survey responses from employees, with features such as:
    Key Features
        - WorkHoursPerWeek: Weekly working time
        - SleepHours: Daily average sleep
        - ManagerSupportScore: Rated support from management
        - CareerGrowthScore: Perceived career advancement
        - BurnoutLevel: Burnout on a scale
        - BurnoutRisk: Categorical risk (High / Low)
        - ProductivityScore, JobSatisfaction, PhysicalActivityHrs
        - Demographic and role information
