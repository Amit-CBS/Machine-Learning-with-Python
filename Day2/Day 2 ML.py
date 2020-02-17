#!/usr/bin/env python
# coding: utf-8

# In[7]:


def f1():
    x=100
    print(x)
f1()
x+=1
print(x)


# In[8]:


#list
l=[3,4.6,"python",45,2.36]
print(l)


# In[9]:


l[-4:-8]#we cant go from -4 to -8 without -ve step


# In[12]:


#adding one value in list
l.append(10)
print(l)


# In[14]:


#adding more than one element
l.extend([20,30,40])
print(l)


# In[17]:


#insert at given index
l.insert(3,56.23)
l


# In[19]:


#copy
l1=l.copy()
l1


# In[20]:


#length
len(l)


# In[22]:


#counting no. of occurence of item
l.count(10)


# In[27]:


l


# In[28]:


#pop 

l.pop(0)#passig index


# In[29]:


l.pop()


# In[30]:


l


# In[32]:


#reverse list
l.reverse()
l


# In[33]:


l.pop(0)


# In[35]:


#sort=>default ascending 
l.sort(reverse=True)
l


# In[1]:


list=[]
for i in range(10):
    a=input()
    list.append(a)
list


# In[2]:


#tuple=>immutable
t=(1,2,3)
t


# In[3]:


#dictionary=>key : value pair where key are treated as index and key must be unique within  in the dictionary otherwise overriden will take place
d={100:"python",2.5:89856,30:2.25,'k':5633}


# In[4]:


d


# In[5]:


d[100]


# In[6]:


d['k']


# In[7]:


d1={2:4.25,'1':'python',9:5620,100:5656262}


# In[8]:


d1[90]=2323


# In[9]:


d1


# In[23]:


#update
d1.update({2:100})
d1


# In[15]:


#pop =>it must contain key otherwise it will through error 
d1.pop(90)
d1


# In[16]:


#popping last item
d1.popitem()


# In[18]:


#set=>unorderd,contain unique item
#create empty set=>call set class
s=set()


# In[19]:


s


# In[20]:


#adding one value inot set
s.add(3)
s


# In[22]:


#adding more than  one value
s.update({2,5})
s


# In[25]:


s1={5,6,20,"111"}
s1.intersection(s)#intersection 


# In[26]:


#union 
s1.union(s)


# In[27]:


#difference=>s1-s=>item present in s1 but not is
s1.difference(s)


# In[28]:


#Numpy=>Numerical python is a module in which we can do mathematical and logiacal operations easily
#installing module in conda after open anacoda cmd
#conda install -u numpy    =>u means update


# In[1]:


import numpy as np


# In[30]:


#1 D array
a1=np.array({1:9090,8:2323})


# In[31]:


a1


# In[32]:


a2=np.array([5,7,8,9])
a2


# In[33]:


a2.dtype


# In[34]:


a3=np.array([5,6,7,8,9,2.0])
a3


# In[36]:


a3.dtype#=>getting float bcz array is collection of same type item ,since it contain 1 float value therefore it converts all value into float 


# In[37]:


a4=np.array([1,2,"python"]) #u=>unicode means all values are into string
a4


# In[38]:


a4.shape #=>row and column


# In[39]:


a4.ndim#dimension


# In[43]:


#range
a5=np.arange(1,20,2)
a5


# In[45]:


a5.sum()


# In[48]:


a6=np.linespace(1,20,11)
a6


# In[49]:


#2d array
ar1=np.array([3,3.9,23,12,45,20]).reshape(3,2)


# In[50]:


ar1


# In[51]:


ar1[1]


# In[52]:


ar1[1,1]


# In[53]:


#slicing in 2 D
#row slicing and coloumn slicing
ar1[1:,:]


# In[10]:


ar2=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]).reshape(5,5)
ar2


# In[11]:


ar2[2:4,1:4]


# In[12]:


ar1[:4]


# In[13]:


ar2.transpose()


# In[3]:


#q1
b1=np.array([])
for i in range(5):
    a=input()
    
    
b1


# In[20]:


b1[0]


# In[21]:


b2=np.array([5,6,7])
j=0
for i in range(b1):
    b[j]=b[j]+i
    j=j+1
b2


# In[5]:


#q3
b3=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]).reshape(4,5)
b3


# In[7]:


b4=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]).reshape(5,4)
b4


# In[14]:


#q4
b3.dot(b4)


# In[17]:


#q5
b5=np.array([10,20,30,40,50,60],ndmin=2)
b5


# In[22]:


b3.


# In[23]:


#pandas=>data analysis library
#pandas=>visualisation is better
#ML=>dataset+algo
#series=>1 D array
#Dataframe=> 2 D array


# In[24]:


import pandas as pd


# In[30]:


#Series
s1=pd.Series([3,4,5,6,7.25,45.25],index=['r1','r2','r3','r4','r5','r6'])
s1


# In[39]:


s2=pd.Series([4,5,6,7,90],index=[i for i in range(len(s2))])
s2


# In[40]:


s3=pd.Series({200:90,25:"kolkata",5:4545})
s3


# In[47]:


#Dataframe
df=pd.DataFrame([[3,4,5,6],[5,6,7],[]],columns=['c1','c2','c3','c4'])
df #Nan=>not a number


# In[ ]:


#slicing in Dataframe
#1 iloc()=>index positon 
#2 loc()=>label based 


# In[56]:


df.loc[1:3,'c1':'c3']


# In[60]:


df2=df.iloc[1:3,2:4]
df2


# In[65]:


#joining of dataframe
df3=pd.concat([df,df2])
df3


# In[ ]:




