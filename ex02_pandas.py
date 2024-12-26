import pandas as pd
data={'Name':['John','Alice','Bob'],
'Age':[21,25,35],
'Gender':['Male','Female','Male']}
df = pd.DataFrame(data)
# print(df)

names=df['Name']
ages=df['Age']
# print(names)
#
# print(ages)

males=df[df['Gender']=='Male']
# print(males)

df['Age']=df['Age']+5
# print(df)

