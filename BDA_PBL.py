#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# In[2]:


shopperstop_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\SHOPERSTOP.NS.csv")
shopperstop_data


# In[3]:


shopperstop_data.shape


# In[4]:


shopperstop_data.info()


# In[117]:


shopperstop_data['Date']=pd.to_datetime(shopperstop_data['Date'])


# In[119]:


shopperstop_data.info()


# In[5]:


shopperstop_data.describe()


# In[124]:


print(f"stock prices between{shopperstop_data.Date.min()} {shopperstop_data.Date.max()}")
print(f"total no. of days{(shopperstop_data.Date.min()-shopperstop_data.Date.max()).days}")


# In[6]:


shopperstop_data.isnull().sum()


# In[7]:


plt.figure(figsize=(20,10))
sns.heatmap(shopperstop_data.isnull())


# In[84]:


shopperstop_data.dropna()


# In[87]:


shopperstop_data.columns


# In[88]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=shopperstop_data,x=high_corr_feature[i],y="Close")


# In[8]:


dmart_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\DMART.NS.csv")
dmart_data


# In[10]:


dmart_data.shape


# In[13]:


dmart_data.info()


# In[125]:


dmart_data['Date']=pd.to_datetime(dmart_data['Date'])


# In[15]:


dmart_data.describe()


# In[16]:


dmart_data.isnull().sum()


# In[17]:


plt.figure(figsize=(20,10))
sns.heatmap(dmart_data.isnull())


# In[86]:


dmart_data.dropna()


# In[89]:


dmart_data.columns


# In[90]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=dmart_data,x=high_corr_feature[i],y="Close")


# In[41]:


axis_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\AXISBANK.NS.csv")
shopperstop_data


# In[44]:


axis_data.info()


# In[126]:


axis_data['Date']=pd.to_datetime(axis_data['Date'])


# In[45]:


axis_data.describe()


# In[47]:


axis_data.isnull().sum()


# In[48]:


plt.figure(figsize=(20,10))
sns.heatmap(axis_data.isnull())


# In[91]:


axis_data.dropna()


# In[93]:


axis_data.columns


# In[96]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=axis_data,x=high_corr_feature[i],y="Close")


# In[42]:


icici_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\IBN.csv")
shopperstop_data


# In[49]:


icici_data.info()


# In[127]:


icici_data['Date']=pd.to_datetime(icici_data['Date'])


# In[51]:


icici_data.describe()


# In[52]:


icici_data.isnull().sum()


# In[97]:


icici_data.columns


# In[98]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=icici_data,x=high_corr_feature[i],y="Close")


# In[43]:


tcs_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\TCS.NS.csv")
shopperstop_data


# In[53]:


tcs_data.info()


# In[128]:


tcs_data['Date']=pd.to_datetime(tcs_data['Date'])


# In[54]:


tcs_data.describe()


# In[55]:


tcs_data.isnull().sum()


# In[99]:


tcs_data.dropna()


# In[100]:


tcs_data.columns


# In[101]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=tcs_data,x=high_corr_feature[i],y="Close")


# In[58]:


amdocs_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\DOX.csv")
amdocs_data


# In[62]:


amdocs_data.info()


# In[129]:


amdocs_data['Date']=pd.to_datetime(amdocs_data['Date'])


# In[63]:


amdocs_data.describe()


# In[104]:


amdocs_data.isnull().sum()


# In[107]:


amdocs_data.columns


# In[106]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=amdocs_data,x=high_corr_feature[i],y="Close")


# In[59]:


jet_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\JETAIRWAYS.NS.csv")
jet_data


# In[65]:


jet_data.info()


# In[130]:


jet_data['Date']=pd.to_datetime(jet_data['Date'])


# In[66]:


jet_data.describe()


# In[68]:


jet_data.isnull().sum()


# In[108]:


jet_data.columns


# In[109]:


jet_data.dropna()


# In[110]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=jet_data,x=high_corr_feature[i],y="Close")


# In[61]:


airasia_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\AIRASIA.TW.csv")
airasia_data


# In[69]:


airasia_data.info()


# In[131]:


airasia_data['Date']=pd.to_datetime(airasia_data['Date'])


# In[70]:


airasia_data.describe()


# In[71]:


airasia_data.isnull().sum()


# In[111]:


airasia_data.columns


# In[112]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=airasia_data,x=high_corr_feature[i],y="Close")


# In[72]:


hdfclife_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\HDFCLIFE.NS.csv")
hdfclife_data


# In[75]:


hdfclife_data.info()


# In[132]:


hdfclife_data['Date']=pd.to_datetime(hdfclife_data['Date'])


# In[76]:


hdfclife_data.describe()


# In[77]:


hdfclife_data.isnull().sum()


# In[113]:


hdfclife_data.columns


# In[114]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=hdfclife_data,x=high_corr_feature[i],y="Close")


# In[73]:


apollo_data=pd.read_csv("C:\\Users\\NIKITA\\Desktop\\dataset_pbl\\AMEH.csv")
apollo_data


# In[78]:


apollo_data.isnull().sum()


# In[79]:


apollo_data.info()


# In[133]:


apollo_data['Date']=pd.to_datetime(apollo_data['Date'])


# In[82]:


apollo_data.describe()


# In[115]:


apollo_data.columns


# In[116]:


high_corr_feature=[ 'Open', 'High','Close', 'Low', 'Adj Close', 'Volume']
for i in range(len(high_corr_feature)):
    if i<=9:
        plt.subplot(4,2,i+1)
        plt.subplots_adjust(hspace=1.2,wspace=0.8)
        sns.regplot(data=apollo_data,x=high_corr_feature[i],y="Close")


# In[ ]:




