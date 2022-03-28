import pandas as pd

file = pd.read_excel('./App/job_course.xlsx', index_col=1, header=2, usecols="A:F")

print(file)