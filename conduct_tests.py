import pandas as pd
from scipy import stats

def conduct_tests(df, question1, question2):
  """
  Conduct statistical tests on the given DataFrame to identify significant relationships between the two questions.
  
  Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be analyzed.
    question1 (str): The name of the first question in the DataFrame.
    question2 (str): The name of the second question in the DataFrame.
  
  Returns:
    results (pandas.DataFrame): A DataFrame containing the results of the tests.
  """
  # Create an empty DataFrame to store the test results
  results = pd.DataFrame(columns=['test', 'statistic', 'p_value'])
  
  # Check the data type of the questions
  question1_type = df[question1].dtype
  question2_type = df[question2].dtype

  # If both questions are continuous variables, conduct a Pearson correlation test
  if question1_type == 'float64' and question2_type == 'float64':
    corr, p_value = stats.pearsonr(df[question1], df[question2])
    results = results.append({'test': 'Pearson correlation', 'statistic': corr, 'p_value': p_value}, ignore_index=True)
 
 # If both questions are categorical variables, conduct a chi-square test of independence
  elif question1_type == 'object' and question2_type == 'object':
    contingency_table = pd.crosstab(df[question1], df[question2])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    results = results.append({'test': 'Chi-square test of independence', 'statistic': chi2, 'p_value': p_value}, ignore_index=True)
  
  # If one question is continuous and the other is categorical, conduct an independent t-test
  elif question1_type == 'float64' and question2_type == 'object':
    t, p_value = stats.ttest_ind(df[df[question2] == df[question2].unique()[0]][question1], df[df[question2] == df[question2].unique()[1]][question1])
    results = results.append({'test': 'Independent t-test', 'statistic': t, 'p_value': p_value}, ignore_index=True)
  
  # If one question is categorical and the other is continuous, conduct a one-way ANOVA
  elif question1_type == 'object' and question2_type == 'float64':
    f, p_value = stats.f_oneway(df[df[question1] == df[question1].unique()[0]][question2], df[df[question1] == df[question1].unique()[1]][question2])
    results = results.append({'test': 'One-way ANOVA', 'statistic': f, 'p_value': p_value}, ignore_index=True)

    return results


import pandas as pd
from scipy import stats

def run_all_tests(df):
  """
  Iterate through each possible combination of two questions in the given DataFrame,
  run the appropriate statistical test, and output the results in a table.
  
  Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be analyzed.
  
  Returns:
    results (pandas.DataFrame): A DataFrame containing the results of all the tests.
  """
  # Get the list of questions in the DataFrame
  questions = df.columns[1:]

  # Create an empty DataFrame to store the test results
  results = pd.DataFrame(columns=['question1', 'question2', 'test', 'statistic', 'p_value', 'count', 'mean', 'sum'])

  # crete a list of all possible combinations of two questions
  combinations = [(questions[i], questions[i+j+1]) for i in range(len(questions)) for j in range(len(questions)-i-1)]
  
  # Iterate over each combination 
  for question1, question2 in combinations:
    # Conduct the appropriate test based on the data types
    if df[question1].dtype == 'float64' and df[question2].dtype == 'float64':
        corr, p_value = stats.pearsonr(df[question1], df[question2])
        test = 'Pearson correlation'
        statistic = corr
    elif df[question1].dtype == 'object' and df[question2].dtype == 'object':
        contingency_table = pd.crosstab(df[question1], df[question2])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        test = 'Chi-square test of independence'
        statistic = chi2
    elif df[question1].dtype == 'float64' and df[question2].dtype == 'object':
        t, p_value = stats.ttest_ind(df[df[question2] == df[question2].unique()[0]][question1], df[df[question2] == df[question2].unique()[1]][question1])
        test = 'Independent t-test'
        statistic = t
    elif df[question1].dtype == 'object' and df[question2].dtype == 'float64':
        f, p_value = stats.f_oneway(df[df[question1] == df[question1].unique()[0]][question2], df[df[question1] == df[question1].unique()[1]][question2])
        test = 'One-way ANOVA'
        statistic = f

    # Add the results to the DataFrame
    results = results.append({'question1': question1, 'question2': question2, 'test': test, 'statistic': statistic, 'p_value': p_value}, ignore_index=True)

    return results, combinations
