# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:03:50 2020

@author: BERON INTELLIGENCE
"""


import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import statistics

current_employee_data = pd.read_excel("Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",sheet_name=1, index_col="Emp ID")
current_employee_data

Ex_employee_data = pd.read_excel("Hash-Analytic-Python-Analytics-Problem-case-study-1.xlsx",sheet_name=2, index_col="Emp ID")
Ex_employee_data

# analysing Ex employee satisfaction level data

Ex_satisfaction_level = Ex_employee_data["satisfaction_level"]
mostCommon = Counter(Ex_satisfaction_level.values)
mostCommon = mostCommon.most_common(1)
print(mostCommon)
print("most common employee who left had the satisfaction level = ", mostCommon[0][0], "Satisfaction")

# analysing Ex employee last evaluation data

Ex_last_evaluation = Ex_employee_data["last_evaluation"]
last_evaluation = Counter(Ex_last_evaluation.values)
last_evaluation = last_evaluation.most_common(1)
print(last_evaluation)
print("most common employee who left had the last evaluation = ", last_evaluation[0][0], "Evaluation")


# analysing Ex employee number of project data

Ex_number_project = Ex_employee_data["number_project"]
number_project = Counter(Ex_number_project.values)
number_project = number_project.most_common(1)
print(number_project)
print("most common employee who left had the Number of project = ", number_project[0][0], "Projects")

# analysing Ex employee average montly hours data

Ex_average_montly_hours = Ex_employee_data["average_montly_hours"]
average_montly_hours = Counter(Ex_average_montly_hours.values)
average_montly_hours = average_montly_hours.most_common(1)
print(average_montly_hours)
print("most common employee who left had the Average Monthly hours = ", average_montly_hours[0][0], "Hours")

# analysing Ex employee time spend company data

Ex_time_spend_company = Ex_employee_data["time_spend_company"]
time_spend_company = Counter(Ex_time_spend_company.values)
time_spend_company = time_spend_company.most_common(1)
print(time_spend_company)
print("most common employee who left had the time spend company = ", time_spend_company[0][0], "Hours")

# analysing Ex employee Work accident data

Ex_Work_accident = Ex_employee_data["Work_accident"]
Work_accident = Counter(Ex_Work_accident.values)
Work_accident = Work_accident.most_common(1)
print(Work_accident)
print("most common employee who left had the Work Accident = ", Work_accident[0][0], "Accidents")

# analysing Ex employee promotion in last 5years data

Ex_promotion_last_5years = Ex_employee_data["promotion_last_5years"]
promotion_last_5years = Counter(Ex_promotion_last_5years.values)
promotion_last_5years = promotion_last_5years.most_common(1)
print(promotion_last_5years)
print("most common employee who left had the Promotion in last 5 years = ", promotion_last_5years[0][0], "Promotion")


# analysing Ex employee Department data

Ex_dept = Ex_employee_data["dept"]
dept = Counter(Ex_dept.values)
dept = dept.most_common(1)
print(dept)
print("most common employee who left was in", dept[0][0], "Department")


# analysing Ex employee Salary data

Ex_salary = Ex_employee_data["salary"]
salary = Counter(Ex_salary.values)
salary = salary.most_common(1)
print(salary)
print("most common employee who left had", salary[0][0], "Salary")



#UNIVARIATE ANALYSIS

#UNIVARIATE ANALYSIS FOR BOTH EMPLOYEES WHO LEFT

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(Ex_employee_data['salary'])
plt.title('Distribution of salaries of Employees who left the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


#UNIVARIATE ANALYSIS FOR EXISTING EMPLOYEES

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(current_employee_data['salary'])
plt.title('Distribution of salaries of Existing Employees in the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()


#department Bar plots for employees who left
plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(Ex_employee_data['dept'])
plt.title('Departments of Employees who left the Company')
plt.tight_layout()

#department Bar plots for existing employees
plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.countplot(current_employee_data['dept'])
plt.title('Departments of Existing Employee ')
plt.tight_layout()

#Satisfaction level for Employees who left
plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=Ex_employee_data)
plt.ylim([0,1])
plt.title('Distribution of satisfaction level of Employees that left by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()

#Satisfaction level for Current Employees 
plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
sns.boxplot(x='dept', y='satisfaction_level', data=current_employee_data)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.1))
plt.title('Distribution of satisfaction level of Existing Employees by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.tight_layout()


# From the box plot of both Existing employees and employees who left the company, the following insights have been discovered 
# The mean satisfaction level of employees who left the company ranges bewteen 40-50% 
# The mean satisfaction level of existing employees in the company ranges between 60-70%
# Performing further analysis on the satisfaction level of both employees who left and existing employees in the company for better insight 

plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = Ex_employee_data)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)


plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept',y='satisfaction_level',hue='salary',data= current_employee_data)
plt.title('Satisfaction level by dept based on the Salary of Existing Employee')
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.tight_layout()
plt.legend(loc=2)

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(Ex_employee_data['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Employees who left')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()

Ex_employee_data['satisfaction_level2'] = pd.cut(Ex_employee_data['satisfaction_level'], 
       3, labels=["small", "medium", "high"])

Ex_employee_data.satisfaction_level2.value_counts()

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(Ex_employee_data['satisfaction_level2'])
plt.title('Distribution Range of satisfaction_level of Employees who left')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(current_employee_data['satisfaction_level'])
plt.title('Distribution of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()

current_employee_data['satisfaction_level2'] = pd.cut(current_employee_data['satisfaction_level'], 
       3, labels=["small", "medium", "high"])
current_employee_data.satisfaction_level2.value_counts()

plt.figure(figsize=(10,7))
sns.set(style='darkgrid')
plt.hist(current_employee_data['satisfaction_level2'])
plt.title('Distribution Range of satisfaction_level of Existing Employees')
plt.xlabel('satisfaction_level')
plt.ylabel('Frequency')
plt.tight_layout()


# From the satisfaction level chart plots of employees who left the company, it is observed that the satisfaction level is below average, 
# therefore it is vital to show the percentage of employees who left that are in this category 

# DETERMINING THE PERCENTAGE OF EMPLOYEES WHO LEFT THE COMPANY HAD A SATISFACTION LEVEL BELOW AVERAGE OF 45
(len(Ex_employee_data[Ex_employee_data['satisfaction_level']<0.45])/len(Ex_employee_data)) * 100


# From the output generated it can be observed that an estimate of 65% of employees who left had a satisfaction level below average of 45%. This needs to be 
# looked into as it's a determining factor as to why employees left the company. Futher insights needs to be carried out as to why the satisfaction level is low. 
#Promotion status, salary where two factors that was considered by intuition which prompted further analysis to determine the percenatge of employees who left having a satisfaction level of 45%, their promotion status and salary range

(Ex_employee_data[Ex_employee_data['satisfaction_level']<0.45] ['salary'].value_counts(normalize=True))*100
#From the output displayed, it can be seen that an estimate of 61% of employees who left where low income earners, 37% where medium income earners and 2% where high income earners.

(Ex_employee_data[Ex_employee_data['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100
# From the output displayed, it can be seen that 99.6% of employees who left had a satisfaction level less than 45% and where not promoted in the last five years

# Through the insights gained from the employees who left, it is vital to validate the position of the existing employees in the company.

# DETERMINING THE MEAN SATISFACTION LEVEL OF EXISTING EMPLOYEES

statistics.mean(current_employee_data['satisfaction_level'])*100
# From the output it is seen that the average satisfaction level of existing employees is estimated around 67%. 
# Hence using the metrics/determing factor of employees who left as an insight to crosscheck existing employees who are prone to leave the company considering their promotion status


(len(current_employee_data[current_employee_data['satisfaction_level']<0.45])/len(Ex_employee_data)) * 100

(current_employee_data[current_employee_data['satisfaction_level']<0.45] ['promotion_last_5years'].value_counts(normalize=True))*100
# From the result displayed it shows 44% of existing employees have a satisfaction level below 45% and from this it is seen that an estimate of 98% have not been promoted in the last 5 years




# BI/MULTIVARIATE ANALYSIS

plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = Ex_employee_data)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of Employees who left')
plt.tight_layout()
plt.legend(loc=2)

plt.figure(figsize=(14,7))
sns.set(style='darkgrid')
sns.barplot(x='dept', y='satisfaction_level', hue='salary', data = current_employee_data)
plt.ylim([0,1])
plt.yticks(np.arange(0, 1, step=0.05))
plt.title('Satisfaction level by Dept based on the Salary of  Existing Employees')
plt.tight_layout()
plt.legend(loc=2)

Ex_employee_data_PRO =Ex_employee_data.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
Ex_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")

# Insight: Most employees who left with a high salary range weren't promoted,regardless of other employee who were promoted that had their salary range from low to medium,
# it futher can be seen that the satisfaction level was below average of 45% and the employees who left where not promoted irrespective of their salary income. 
 # Hence Satisfaction level and promotion status are determining factors as to why employees are leaving the company.

current_employee_data_PRO =current_employee_data.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
current_employee_data_PRO.plot.bar()
plt.title(" Satisfaction Level of Existing Employee based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)

# The insight obtained from this ouput for employees still existing in the company is such that salary is not a determining factor 
# as to why the existing employees should leave the company due to the fact that the employees satisfaction level is above an average of 50% 
# irrespective of their promotion status.


Ex_employee_data_PRO =Ex_employee_data.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
Ex_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Employee who left based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")

# From output above the insight: 
# Time Spent and promotion status are great factors that determine if an employee should leave or not, 
# some employee who left that spent 6 years in the company weren't promoted, even though their satisfaction level was quite moderate.
# It can also be seen that An avaerge employee who left spent about 4 years with 0.45 satisfaction level and wasn't promoted. 


current_employee_data_PRO =current_employee_data.pivot_table(index='time_spend_company',columns='promotion_last_5years',values='satisfaction_level')
current_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Time Spent in the company and promotion Status")
plt.xlabel("Time Spent")
plt.ylabel("Satisfaction Level")
plt.legend(loc=2)

# From the output the insight obtained is such that the existing employees in company irrespective of the time spent 
# have a moderate satisfaction level and positive promotion status above 0.5 exculding employeees that spent between 5 years in the company. 
# Hence satisfaction level of employees that spent 5 years should is considered as a determining factor and why such employees are prone to leave.

Ex_employee_data_PRO =Ex_employee_data.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
Ex_employee_data.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and work accident")
plt.xlabel("Salary")
plt.ylabel("Satisfaction Level")

# From the output the insight obtained is such that employees who left that earn between low and medium salaries where affected by work accidents 
# and their satisfaction level was below avaerage of 0.45 as compared to those with a high salary. 
# Hence work accident and satisfaction level are reasons as to why employees are leaving the company.


current_employee_data_PRO =current_employee_data.pivot_table(index='salary',columns='Work_accident',values='satisfaction_level')
current_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Salary in the company and work accident")
plt.xlabel("salary")
plt.ylabel("Satisfaction Level")

Ex_employee_data_PRO =Ex_employee_data.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
Ex_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")

# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by employees who left exceeded 4, 
# the satisfaction level began to decline and they where not promoted in the last five years. 
# Hence an increase in the number of projects resulting in a decline in satisfaction level and 
# employee promotion status can be seen as reasons as to why employees are leaving the company.

current_employee_data_PRO =current_employee_data.pivot_table(index='number_project',columns='promotion_last_5years',values='satisfaction_level')
current_employee_data_PRO.plot.bar()
plt.title("Satisfaction Level of Existing Employee based on Number of Projects and Promotion Status")
plt.xlabel("Number Project")
plt.ylabel("Satisfaction Level")

# From the output displayed, the insight gotten it can be seen that as the number of projects embarked on by
#  employees still in the company exceeded 4, the satisfaction level began to decline and they where not promoted in the last five years, 
# this can also be seen as a trend for employees who left. Hence an increase in the number of projects 
# resulting in a decline in satisfaction level and 
# employee promotion status can be seen as reasons as to which exsiting employees are prone to leave the company.



#Evaluations on factors for employees who left

print("most common employee who left had the satisfaction level = ", mostCommon[0][0], "Satisfaction")
print("most common employee who left had the last evaluation = ", last_evaluation[0][0], "Evaluation")
print("most common employee who left had the Number of project = ", number_project[0][0], "Projects")
print("most common employee who left had the Average Monthly hours = ", average_montly_hours[0][0], "Hours")
print("most common employee who left had the time spend company = ", time_spend_company[0][0], "Hours")
print("most common employee who left had the Work Accident = ", Work_accident[0][0], "Accidents")
print("most common employee who left had the Promotion in last 5 years = ", promotion_last_5years[0][0], "Promotion")
print("most common employee who left was in", dept[0][0], "Department")
print("most common employee who left had", salary[0][0], "Salary")


# Type of employee who left 

employee_who_left = {mostCommon[0][1]:mostCommon[0][0],last_evaluation[0][1]:last_evaluation[0][0],number_project[0][1]:number_project[0][0],average_montly_hours[0][1]:average_montly_hours[0][0],
                     time_spend_company[0][1]:time_spend_company[0][0],Work_accident[0][1]:Work_accident[0][0],
                     promotion_last_5years[0][1]:promotion_last_5years[0][0],dept[0][1]:dept[0][0],salary[0][1]:salary[0][0]}

print(employee_who_left)

#type of employee who left
print("type of employee who left are the ones who got ",promotion_last_5years[0][0], "Promotion in 5 Years", "Total number of that employess are" ,max(employee_who_left.keys()))



#prediction with signinficant values

leaving = current_employee_data[(current_employee_data.dept == dept[0][0]) &
                      (current_employee_data.salary == salary[0][0])&
                     (current_employee_data.promotion_last_5years == promotion_last_5years[0][0])&
                      (current_employee_data.number_project <= number_project[0][0])
                      ] 



#strong prediction for the employee who prone to leave in future from current employee data
current_employee_data[(current_employee_data.satisfaction_level < max(Ex_satisfaction_level)) & 
                      (current_employee_data.dept == dept[0][0]) &
                      (current_employee_data.salary == salary[0][0])&
                     (current_employee_data.promotion_last_5years == promotion_last_5years[0][0])&
                      (current_employee_data.time_spend_company == time_spend_company[0][0])&
                      (current_employee_data.last_evaluation <= last_evaluation[0][0])&
                      (current_employee_data.number_project <= number_project[0][0])&
                      (current_employee_data.average_montly_hours <=average_montly_hours[0][0])&
                      (current_employee_data.Work_accident == Work_accident[0][0])
                      ] 

print(leaving)


import openpyxl
leaving.style.\
    to_excel('Prone_to_leave.xlsx', engine='openpyxl')