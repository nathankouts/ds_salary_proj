# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:12:40 2020

@author: Nathan
"""

import pandas as pd

df = pd.read_csv('C:/Users/Nathan/Documents/ds_salary_proj/glassdoor_jobs.csv')

#salary parsing


df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower()else 0)
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower()else 0)

#Get rid of -1 from salary estimate
df = df[df['Salary Estimate'] != '-1']

#get rid of glassdoor estimate text
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#get rid of $ and K
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#get rid of per hour, employer provided salary and ':'
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary','').replace(':',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2


#Company name text only
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

#check to see if job location is in the same place as the headquarters
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#calculate the age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#parsing of job description (python, etc.)
df['Job Description'][0]

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#rstudio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#AWS
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

