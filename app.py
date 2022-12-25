import streamlit as st
import pandas as pd
from conduct_tests import conduct_tests, run_all_tests

def main():
  st.title('Statistical Tests')

  # Allow the user to upload a CSV file
  uploaded_file = st.file_uploader('Upload a CSV file', type='csv')
  if uploaded_file is None:
    st.write('Please upload a CSV file to continue.')
    return

  # Load the CSV file into a DataFrame
  df = pd.read_csv(uploaded_file)
  # convert all int64 to float64
  df = df.astype('float64')
  # identify the column types, display the column name and type

  st.write(df.dtypes)
  results_all = run_all_tests(df)
  st.write(results_all)

  # Get the list of questions in the DataFrame
  questions = df.columns[1:]

  # Allow the user to select two questions
  question1 = st.selectbox('Select the first question', questions)
  question2 = st.selectbox('Select the second question', questions)

  # Conduct the tests
  results = conduct_tests(df, question1, question2)

   # Display the results
  st.write(results)



  



 

if __name__ == '__main__':
  main()


