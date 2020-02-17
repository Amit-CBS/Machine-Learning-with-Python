#!/usr/bin/env python
# coding: utf-8

# In[7]:


x=eval(input("Enter the value:"))#eval=>it can take int ,float etc...
print(x)


# In[8]:


def fact(n):
    f=i=1
    while(i<=n):
        f=f*i
        i+=1
    return f


# In[9]:


fact(5)


# In[14]:


a=eval(input("Enter the number :"))
for j in range(2,a):
    if a%j==0:
        print("Not prime")
        break
    elif j==a-1:
        print("prime")
        
    


# In[9]:


def fibo(n):#positional argument
    i=3
    a,b=0,1
    print(a,b,end=" ")
    while(i<=n):
        
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i+=1
        


# In[10]:


fibo(5)


# In[11]:


def nametest(name,age):
    print("name is :",name)
    print("age is :",age)


# In[12]:


nametest("abc",20)#positional argument
nametest(age=21,name="xyz")#keyword argument
                           #varible argument =>def nameoffunction(*t):


# In[13]:


#varible argument
def test4(*t):#t=>tuple
    for i in t:
        print(i)


# In[14]:


test4(1,"kolkata")


# In[15]:


#lambda funtion
#lambda a,b:expression
s=lambda a,b:a+b


# In[16]:


s(6,9)


# In[4]:


import os


# In[6]:


os.chdir(r"C:\Users\amark\Desktop")#row string 


# In[7]:


os.getcwd()


# In[8]:


import modl


# In[10]:


modl.test(2,3)


# In[22]:


from modl import test


# In[23]:


#class
class test_class:
    m,n=3,4
    def input1(self):
        p=self.m+self.n
        print(p)
        


# In[24]:


#creation of object 
ob=test_class()
ob.input1()


# In[25]:


#constructor
class B:
    def __init__(self,k,l):
        self.k=k
        self.l=l
        z=self.k+self.l
        print(z)


# In[26]:


obj=B(5,10,)


# In[27]:


help(str)


# In[28]:


#string 
s="machine learning with python"#s is object of the class str3
# shift+tab=>gives suggestion inside function parenthesis


# In[ ]:


#string.tab=>get suggestion 

