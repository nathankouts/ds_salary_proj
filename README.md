# Data Science Salary Predictor
  * Created a tool that predicts data science salaries based on some features.
  *	Scraped over 1000 job descriptions from glassdoor using python.

  *	Analyzed the text of each job description to see the value that companies put on python, excel, aws, and spark.

  *	Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

  *	Built a client facing API.



# Web Scraping
I scraped job openings from glassdoor.com and categorized the information in the following columns:

 * Job title
 * Salary Estimate
 * Job Description
 * Rating
 * Company
 * Location
 * Company Headquarters
 * Company Size
 * Company Founded Date
 * Type of Ownership
 * Industry
 * Sector
 * Revenue
 * Competitors
 
 # Data Cleaning
 After I was done with scraping the data, I needed to clean it up so that it could be used for modelling. I made the following changes and created the following variables:

 * Parsed numeric data out of salary
 * Made columns for employer provided salary and hourly wages
 * Removed rows without salary
 * Parsed rating out of company text
 * Made a new column for company state
 * Added a column for if the job was at the company’s headquarters
 * Transformed founded date into age of company
 * Made columns for if different skills were listed in the job description:
    * Python
    * R
    * Excel
    * AWS
    * Spark
 * Column for simplified job title and Seniority
 * Column for description length
 
 # Exploratory Data Analysis (EDA)
 I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
 
![alt text](https://github.com/nathankouts/ds_salary_proj/blob/master/job_by_salary.png?raw=true)
![alt text](https://github.com/nathankouts/ds_salary_proj/blob/master/job_state.png?raw=true)
![alt text](https://github.com/nathankouts/ds_salary_proj/blob/master/corr.png?raw=true)
 
# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

 * Multiple Linear Regression – Baseline for the model
 * Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso    would be effective.
 * Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.
 
 
 # Model Performance
 The Random Forest model far outperformed the other approaches on the test and validation sets.
  * **Random Forest**: MAE = 11.22
  * **Linear Regression**: MAE = 18.86
  * **Ridge Regression**: MAE = 19.67
  
 # Productionization
 In this step, I built a Flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
