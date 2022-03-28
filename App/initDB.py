import pandas as pd

file = pd.read_excel('./App/job_course.xlsx', index_col=0, header=0, usecols="A:F")

print(file)