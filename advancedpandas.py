import pandas as pd

#periods make pandas confused as it thinks its a function, ex: "location.citizenship"
# use `` to bypass this
df = pd.read_csv('billionaires.csv')

df = df.query('`location.citizenship` == "United States"')

print(df.columns)





