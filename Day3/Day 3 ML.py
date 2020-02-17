#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


#dataset
data1={'Name':['Amar','Anupam','Anshuman'],
      'Roll':[104,94,95],
      'qualification':['B.Tech','B.Tech','B.Tech'],
      }

data2={'Name':['Anvesh','Krishna','ABhishek'],
      'Roll':[92,66,100],
      'qualification':['B.Tech','B.Tech','B.Tech'],
      }


# In[8]:


#Creating dataframe 1
df1=pd.DataFrame(data1,index=[0,1,2])
df1


# In[9]:


#creating Dataframe 2
df2=pd.DataFrame(data2,index=[3,4,5])
df2


# In[10]:


#concatenation
pd.concat([df1,df2])


# In[11]:


#dataset
data3={'Name':['Amar','Anupam','Anshuman'],
      'Roll':[104,94,95],
      'qualification':['B.Tech','B.Tech','B.Tech'],
      }


data4={'Adress':['jharkhand','Bihar','Kolkata'],
      'Roll':[104,94,95],
      'Age':[100,101,102],
      }



# In[12]:


#creating Dataframe 3
df3=pd.DataFrame(data3)
df3


# In[13]:


#creating Dataframe 4
df4=pd.DataFrame(data4)
df4


# In[14]:


#merge function()
res=pd.merge(df3,df4,on="Roll")
res


# In[17]:


res=df1.append(df2)
res


# In[18]:


#reading csv file and converting into dataframe
weather=pd.read_csv(r"C:\Users\amark\Downloads\weather.csv")
weather


# In[19]:


weather.shape


# In[21]:


weather.head()


# In[22]:


weather.tail()


# In[26]:


w=weather.iloc[10:21,0:3]
w


# In[27]:


x=weather.iloc[:5,0]
y=weather.iloc[:5,1]


# In[28]:


import matplotlib.pyplot as plt


# In[29]:


plt.plot(x,y)


# In[30]:


plt.scatter(x,y)


# In[31]:


plt.hist(y)


# In[35]:


#feature engineering




#checking missing values
weather.isnull().sum()


# In[36]:


#printing maximum temperature column
weather['maximum temperature']


# In[39]:


#filling missing values with mean median mode function
weather['maximum temperature'].fillna(weather['maximum temperature'].mean(),inplace=True)
weather


# In[40]:


weather.isnull().sum()


# In[42]:


#mode return list nd 0 index return most frequent one
weather['snow fall'].fillna(weather['snow fall'].mode()[0],inplace=True)
weather


# In[43]:


weather.isnull().sum()


# In[44]:


#method inside fillna() fill the missing place with forward or backward value usin ffill or bfill
weather['snow depth'].fillna(method="ffill",inplace=True)
weather


# In[45]:


weather.isnull().sum()


# In[ ]:




