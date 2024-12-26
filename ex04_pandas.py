import pandas as pd

data={'A':[1,2,2,3],
'B':['X','Y','Y','Z']}
df=pd.DataFrame(data)
# print(df)

# duplicates=df.duplicated()
# print(duplicates)

df.drop_duplicates(inplace=True)
print(df)