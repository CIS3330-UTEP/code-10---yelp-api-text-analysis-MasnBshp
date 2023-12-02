import pandas as pd


df = pd.read_csv('billionaires.csv')

print(df.sort_values(by='name'))

#get only a few columns to a new file/subversion