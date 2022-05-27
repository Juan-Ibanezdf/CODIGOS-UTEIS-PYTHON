# Read and Write CSV
# pip install pandas
import pandas as pd
# Reading csv
df = pd.read_csv('data.csv')
print(df)
# Reading csv specific column
df = pd.read_csv('data.csv', usecols=['Name', 'Email'])
print(df)
# Reading csv specific row
df = pd.read_csv('data.csv', nrows=2)
print(df)
# Reading csv specific row and column
df = pd.read_csv('data.csv', nrows=2, usecols=['Name', 'Email'])
print(df)
# Convert data to List
df = pd.read_csv('data.csv')
df = df.values.tolist()
# Convert Column to list
df = pd.read_csv('data.csv')        
df = df['Name'].tolist()
# Convert Row to list
df = pd.read_csv('data.csv')
df = df.iloc[0].tolist()
# Writing csv
Dataframe = {'Name': ['John', 'Smith'], 'Age': [20, 30]}
df = pd.DataFrame(Dataframe)
df.to_csv('data.csv', index=False)
# Appending CSV
Dataframe = {'Name': ['John', 'Smith'], 'Age': [20, 30]}
df = pd.read_csv(Dataframe)
df.to_csv('data.csv', mode='a', index=False, header=False)