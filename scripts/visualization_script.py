# script for visualizing the data

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# import user-defined functions
from data.load import load_data

# root directory
cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(cur_dir, "..")

# load data
df = load_data(preprocessed=True)

# attrition distribution
plt.subplots(figsize=(10, 6))
sns.countplot(x='Attrition', data=df, color='skyblue')
plt.title('Attrition Count')
plt.xlabel('Attrition')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.savefig(root_dir+'/reports/figures/attrition_count.png')
plt.show()


# work time per day vs attrition
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df[df['Attrition'] == 0]['WorkTimePerDay'], color='skyblue', label='No Attrition', fill=True, ax=ax)
sns.kdeplot(data=df[df['Attrition'] == 1]['WorkTimePerDay'], color='red', label='Attrition', fill=True, ax=ax)

plt.axvline(df[df['Attrition'] == 0]['WorkTimePerDay'].mean(), color='skyblue', linestyle='dashed', linewidth=1)
plt.axvline(df[df['Attrition'] == 1]['WorkTimePerDay'].mean(), color='red', linestyle='dashed', linewidth=1)

plt.title('Time Spent in Office vs Attrition')
plt.xlabel('Time Spent in Office (seconds)')
plt.ylabel('')
plt.yticks([])
plt.legend()
plt.savefig(root_dir+'/reports/figures/worktimeperday.png')
plt.show()


# monthly income vs attrition
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df[df['Attrition'] == 0]['MonthlyIncome'], color='skyblue', label='No Attrition', fill=True, ax=ax)
sns.kdeplot(data=df[df['Attrition'] == 1]['MonthlyIncome'], color='red', label='Attrition', fill=True, ax=ax)

plt.axvline(df[df['Attrition'] == 0]['MonthlyIncome'].mean(), color='skyblue', linestyle='dashed', linewidth=1)
plt.axvline(df[df['Attrition'] == 1]['MonthlyIncome'].mean(), color='red', linestyle='dashed', linewidth=1)

plt.title('Monthly Income vs Attrition')
plt.xlabel('Monthly Income (USD)')
plt.ylabel('')
plt.yticks([])
plt.legend()
plt.savefig(root_dir+ '/reports/figures/income.png')
plt.show()


# age vs attrition
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df[df['Attrition'] == 0]['Age'], color='skyblue', label='No Attrition', fill=True, ax=ax)
sns.kdeplot(data=df[df['Attrition'] == 1]['Age'], color='red', label='Attrition', fill=True, ax=ax)

plt.axvline(df[df['Attrition'] == 0]['Age'].mean(), color='skyblue', linestyle='dashed', linewidth=1)
plt.axvline(df[df['Attrition'] == 1]['Age'].mean(), color='red', linestyle='dashed', linewidth=1)

plt.title('Age vs Attrition')
plt.xlabel('Age')
plt.ylabel('')
plt.yticks([])
plt.legend()
plt.savefig(root_dir + '/reports/figures/age.png')
plt.show()


# distance from home vs attrition
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df[df['Attrition'] == 0]['DistanceFromHome'], color='skyblue', label='No Attrition', fill=True, ax=ax)
sns.kdeplot(data=df[df['Attrition'] == 1]['DistanceFromHome'], color='red', label='Attrition', fill=True, ax=ax)

plt.axvline(df[df['Attrition'] == 0]['DistanceFromHome'].mean(), color='skyblue', linestyle='dashed', linewidth=1)
plt.axvline(df[df['Attrition'] == 1]['DistanceFromHome'].mean(), color='red', linestyle='dashed', linewidth=1)

plt.title('Distance From Home vs Attrition')
plt.xlabel('Distance From Home')
plt.ylabel('')
plt.yticks([])
plt.legend()
plt.savefig(root_dir+'/reports/figures/disthome.png')
plt.show()


# percent salary hike vs attrition
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df[df['Attrition'] == 0]['PercentSalaryHike'], color='skyblue', label='No Attrition', fill=True, ax=ax)
sns.kdeplot(data=df[df['Attrition'] == 1]['PercentSalaryHike'], color='red', label='Attrition', fill=True, ax=ax)

plt.axvline(df[df['Attrition'] == 0]['PercentSalaryHike'].mean(), color='skyblue', linestyle='dashed', linewidth=1)
plt.axvline(df[df['Attrition'] == 1]['PercentSalaryHike'].mean(), color='red', linestyle='dashed', linewidth=1)

plt.title('Percentage Salary Increase vs Attrition')
plt.xlabel('Percentage Salary Increase')
plt.ylabel('')
plt.yticks([])
plt.legend()
plt.savefig(root_dir + '/reports/figures/salaryhike.png')
plt.show()