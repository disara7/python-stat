import pandas as pd

data={'A':[1,2,None,4],
      'B':[5,None,7,8]}
df=pd.DataFrame(data)
# print(df)

# missing=df.isnull()
# print(missing)

df.fillna(0,inplace=True)
print(df)

