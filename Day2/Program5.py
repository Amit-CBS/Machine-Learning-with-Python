import pandas as pd
df=pd.DataFrame(columns=['Name','Roll no.'])
print(df)
data = [pd.Series(['Amit', 56], index=df.columns ) , pd.Series(['Raj', 57], index=df.columns ) , pd.Series(['Singh', 58], index=df.columns ),pd.Series(['Shashwat', 59], index=df.columns ),pd.Series(['Aniket', 60], index=df.columns ),pd.Series(['Sinha', 61], index=df.columns ),pd.Series(['Kumar', 62], index=df.columns ) ]
new_df = df.append(data)
print("\nDataFrame with values:\n",new_df)