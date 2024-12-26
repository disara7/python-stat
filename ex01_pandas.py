import pandas as pd
data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,10,26]}
df=pd.DataFrame(data)

# print(df)
#
# print(df.head(2))

# ages=df['Age']
# print(ages)

# row=df.iloc[0]
# print(row)

# adults=df[df['Age']>=18]
# print(adults)

df["Gender"]=["Female","Male","Male"]
# print(df)

# summary=df.describe()
# print(summary)

# grouped = df.groupby('Gender')['Age'].mean()
# print(grouped)

df.to_csv('my_data.csv',index=False)