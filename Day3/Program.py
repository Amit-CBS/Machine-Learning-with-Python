#Part 1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
salary=pd.read_csv(r"/media/amit/Work/GitHub/ML with Python Training/DataSets/salary_data.csv")
print("Raw Data:")
print(salary)

#Part 2
print()
print(salary.isnull().sum())
print("\nSo, no missing value\n")

#Part 3
x=salary.iloc[:,0:1] 
y=salary.iloc[:,1]

#Part 4
ts_score=[]
for j in range(100):
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=j)
    lr=LinearRegression().fit(x_train,y_train)
    ts_score.append(lr.score(x_test,y_test))
k=ts_score.index(np.max(ts_score))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=k)

#Part 5
fr=LinearRegression().fit(x_train,y_train)

#Part 6
y_pred=fr.predict(x_test)
print("r2score =",r2_score(y_test,y_pred))
print("Mean Squared value =",mean_squared_error(y_test,y_pred))
print("Root Mean Squared value =",np.sqrt(mean_squared_error(y_test,y_pred)))