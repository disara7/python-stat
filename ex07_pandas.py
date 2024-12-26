import pandas as pd

df=pd.read_csv('my_data.csv')
# print(df)

df['Age']=df['Age']+5
# print(df)

df.rename(columns={'Age':'Student_Age'}, inplace=True)
print(df)