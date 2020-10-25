# Data Science Salary Project

Still in progress...

# Data Science Salary Predictor
  * Created a tool that predicts data science salaries based on some features.
  *	Scraped over 1000 job descriptions from glassdoor using python.

  *	Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.

  *	Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.

  *	Built a client facing API.



# Web Scraping
Tweaked the web scraper to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

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
 After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

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
