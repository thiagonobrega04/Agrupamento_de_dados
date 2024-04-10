import pandas as pd

df = pd.DataFrame({'StudentAge': [10, 12, 14, 9, 15, 19, 17, 12, 10, 14]})
bins = [0, 9, 12, 15, 19]
labels = ["grade1", "grade2", "grade3", "grade4"]
df['GradeLevel'] = pd.cut(df['StudentAge'], bins, labels=labels)
print(df)

# Now, let's modify the bins' edges in the binning process. Currently, bins' edges poorly represent the given dataset, resulting in most students getting NaN as their bin. Let's adjust the bins' edges so all the students are included.

grades = pd.DataFrame({'student_ages': [9, 12, 14, 11, 15, 14, 12, 10, 17, 17, 16, 10, 14]})
bins = [7, 9, 18] # ajustei o limite superior (antes era 11) => o limite inferior tem que ser um número menor que o menor número fornecido e o limite superior tem que ser um número maior que o maior número fornecido
labels = ['Junior', 'Senior']

# Assign the grades
grades['grade'] = pd.cut(grades['student_ages'], bins, labels=labels)

# Print the results
print(grades)

students = pd.DataFrame({'age': [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]})
groups = ["primary", "middle", "high", "college"]
students['school_level'] = pd.qcut(students['age'], q=4, labels=groups)

print(students)

df = pd.DataFrame({'student_ages': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]})

#TODO: bin ages into age groups using qcut
# Replace the TODO comment with the line of code that assigns the 'age_group' to the dataframe using the pd.qcut() function. Create exactly 4 data bins.
df['age_group'] = pd.qcut(df['student_ages'], q=4, labels=False)

for phase in set(df['age_group']):
    print(f"{phase}: {list(df[df['age_group'] == phase]['student_ages'])}")

education = pd.DataFrame({'Age': [5, 23, 16, 33, 78, 15, 41, 66]})

# TODO: Define bins and labels for the Age Groups
bins = [0, 13, 19, 60, 100]

# For your next challenge, you have the ages of various individuals that you need to categorize into specific age groups: 'Elementary' (0-13 years), 'High School' (14-19 years), 'Adult' (20 - 60 years), and 'Senior' (61-100 years). You must create a column labeled 'Age Group' and assign these labels based on their respective ages.
labels = ['Elementary', 'High School', 'Adult', 'Senior']

# TODO: Create a new column 'Age Group' and apply pd.cut() to categorize ages 
education['Age Group'] = pd.cut(education['Age'], bins, labels=labels)

# TODO: Print the DataFrame
for age_group in set(education['Age Group']):
    print(f"{age_group}: {list(education[education['Age Group'] == age_group]['Age'])}")