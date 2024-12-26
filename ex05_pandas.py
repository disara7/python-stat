import pandas as pd

data={'Name':['John Doe', 'Alice Smith', 'Bob Johnson'],
      'Age':['28','24','22']}
df=pd.DataFrame(data)
# print(df)

df['Name']=df['Name'].str.title()
# print(df)

df['Age']=df['Age'].astype(int)
# print(df)



