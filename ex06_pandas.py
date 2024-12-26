import pandas as pd

data={'score':[95,78,101,80]}
df = pd.DataFrame(data)
# print(df)

df['score']=df['score'].replace(101,pd.NA)
# print(df)

df.rename(columns={'score':'exam_score'},inplace=True)
print(df)

