### Introduction
This function conducts statistical tests on a dataset to identify significant relationships between two questions. The function is written in Python and uses the pandas and scipy libraries.

### How the function works
The function takes a DataFrame containing the dataset and the names of two questions as input. It then determines the data type of each question (continuous or categorical) and selects the appropriate test based on the data types. The function performs one of the following tests:

- **Pearson correlation:** If both questions are continuous variables, the function calculates the Pearson correlation coefficient and p-value to determine if there is a significant relationship between the two variables.

- **Chi-square test of independence:** If both questions are categorical variables, the function calculates the chi-square statistic and p-value to determine if there is a significant association between the two variables.

- **Independent t-test:** If one question is continuous and the other is categorical, the function calculates the t-statistic and p-value to determine if there is a significant difference between the means of the two groups.

- **One-way ANOVA:** If one question is categorical and the other is continuous, the function calculates the F-statistic and p-value to determine if there is a significant difference between the means of the groups.

### Outcome
The function returns a DataFrame containing the results of the tests. The DataFrame includes the name of the test that was conducted, the test statistic (e.g., Pearson correlation coefficient, chi-square statistic), and the p-value.

A p-value less than 0.05 indicates that the relationship between the two questions is statistically significant. This means that the relationship is unlikely to have occurred by chance and is likely to be genuine.

### Example
Here is an example of how to use the function:

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('dataset.csv')

# Conduct the tests
results = conduct_tests(df, 'question1', 'question2')

# Print the results
print(results)

The output of the function might look something like this:

# write the output as a table in markdown
| Test | statistic | p_value |
| --- | --- | --- |
| Pearson correlation | 0.73 | 0.002 |

This output indicates that there is a significant positive correlation (r=0.73, p=0.002) between the two questions.



