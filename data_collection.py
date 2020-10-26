import pandas as pd
import glassdoor_scraper as gs

path = "C:/Users/Nathan/Documents/ds_salary_proj/chromedriver.exe"
df = gs.get_jobs('data scientist', 1000, False, path, 15)
