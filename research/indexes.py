import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(schema_df.loc['MgrIdiot', 'QuestionText'])
