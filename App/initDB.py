import pandas as pd

file = pd.read_excel('./App/job_course.xlsx', index_col=0, header=1)

print(file)