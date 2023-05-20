import pandas as pd 

df1 = pd.read_csv('employee_data.csv')
#print(df1)

first_5_rows = df1.head(5)
print('\n 2.  ',first_5_rows )

avg_age = df1['age'].mean()
print('\n 3. average age is :',avg_age)

max_salary =df1['salary'].max()
print('\n 4. maximum salary among employees is :',max_salary)

only_female = df1[df1['gendre'] == 'female']
print('\n 5. data of female employees only:','\n ', only_female)
#print(df1.info()) 