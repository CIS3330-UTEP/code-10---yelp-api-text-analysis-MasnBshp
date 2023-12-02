import pandas as pd

def get_full_name(row):
    #print(row)
    full_name = row['name'].split()

    return full_name[0]
df = pd.read_csv('billionaires.csv')

# for index, row in df.iterrows():
#     #print(row)
#     full_name = row['name'].split()
#     #print(row['name'].split())
#     # print(full_name[0])
#     # #print(full_name[1:])
#     # print(' '.join(full_name[1:]))
#     # #print(type(row))

#     df.at[index,'First_Name'] = full_name[0]
#     df.at[index,'Last_Name'] = ''.join(full_name[1:])

# print(df[['name','First_Name','Last_Name']])

# df.to_csv('new_data_iterating.csv',index=False)



#Vectorization approach

# df.apply(get_full_name, axis=1)     #does a for loop without the for loop, more efficient but weird

#df['First_Name'] = df.apply(get_full_name, axis=1)  