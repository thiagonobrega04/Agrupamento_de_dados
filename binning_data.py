import pandas as pd

# Implementing Binning Techniques using Pandas
# Pandas offers functions such as cut() and qcut() for binning purposes. Let's dive into a practical example.

df = pd.DataFrame({'ages': [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]})

bins = [17, 25, 35, 60, 100]
labels = ["Youth", "YoungAdult", "MiddleAged", "Senior"]
df['categories'] = pd.cut(df['ages'], bins, labels=labels)

# In the example above, we utilized the pd.cut() function to divide a set of ages into distinct age groups or bins. This approach allows us to categorize a wide range of ages into a selected age group, simplifying data analysis. In this particular case, we have ages 18-25 in the "Youth" bin, ages 26-35 in the "YoungAdult" bin, and so on.

# While using the pd.cut() function, it's noteworthy that the bins we create are generally right-closed intervals. It means they include their right endpoint but exclude their left endpoint. So, in our example, an age of 25 falls into the "Youth" bin (17;25], not in the "YoungAdult" bin (25;35].

# The way it looks in the dataset is that each age is mapped to a category via the "categories" column.

# Let's print out the resulting bins by choosing all the ages for each category separately:

for category in set(df['categories']):
    print(f"{category}: {list(df[df['categories'] == category]['ages'])}")

'''Output:
Youth: [20, 22, 25, 21, 23]
YoungAdult: [27, 31, 32]
MiddleAged: [37, 45, 41]
Senior: [61]
'''

# Binning with qcut
# Now let's consider an example of the qcut() function.

df['categories'] = pd.qcut(df['ages'], q=4)

# Unlike the cut() function, the qcut() function aims to divide the data into bins such that each bin contains nearly the same number of observations.

# Let's print it using the same method:
for category in set(df['categories']):
    print(f"{category}: {list(df[df['categories'] == category]['ages'])}")

'''Output:
(22.75, 29.0]: [25, 27, 23]
(19.999, 22.75]: [20, 22, 21]
(38.0, 61.0]: [61, 45, 41]
(29.0, 38.0]: [37, 31, 32]
'''

# As you can see, bins' boundaries are adjusted so that all the bins contain the same number of values.

# Labelling qcut
# Like with the cut() function, you can specify labels for the bins created by qcut().

labels = ["Q1", "Q2", "Q3", "Q4"]
df['quartile_categories'] = pd.qcut(df['ages'], q=4, labels=labels)

# In this example, we have divided the ages into 4 equal-sized bins (quartiles), and we have labeled these quartiles as Q1, Q2, Q3, and Q4. The labels make understanding each bin's place in data distribution easier.

# We can print this with:

for category in sorted(set(df['quartile_categories'])):
    print(f"{category}: {list(df[df['quartile_categories'] == category]['ages'])}")

'''Output:
Q1: [20, 22, 21]
Q2: [25, 23, 27]
Q3: [31, 37, 32]
Q4: [45, 41, 61]
'''

# As you can see, providing labels to bins makes the quartiles easier to understand and interpret. It's beneficial when dealing with data where the quartiles have a specific meaning or significance.