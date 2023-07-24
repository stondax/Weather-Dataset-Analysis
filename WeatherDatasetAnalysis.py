#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"/Users/user/Documents/Datasets for Practice/1. Weather Data.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.shape


# In[7]:


data.index


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[12]:


data['Weather'].unique()


# In[14]:


data.nunique()


# In[15]:


data.count()


# In[16]:


data['Weather'].value_counts()


# In[17]:


data.info()


# In[18]:


# finding all the unique "Wind Speed" value


# In[19]:


data.head(2)


# In[20]:


data.nunique()


# In[21]:


data['Wind Speed_km/h']


# In[22]:


data['Wind Speed_km/h'].nunique()


# In[23]:


data['Wind Speed_km/h'].unique() #done


# In[24]:


data.head(2)


# In[25]:


#Finding the number of times when the "Weather is exactly Clear"


# In[26]:


# value_counts()
data.Weather.value_counts()


# In[29]:


#Filtering
data.head(2)
data[data.Weather == 'Clear']


# In[30]:


#groupby()
data.groupby('Weather').get_group('Clear')


# In[31]:


#Finding the number of times when the "Wind Speed was exactly 4 km/h"


# In[32]:


data[data['Wind Speed_km/h'] == 4] #done


# In[33]:


#Finding all null values


# In[35]:


data.isnull().sum()


# In[36]:


data.notnull().sum()


# In[37]:


#Renaming the column name "Weather" of the data frame to "Weather Condition"


# In[38]:


data.rename(columns = {'Weather': 'Weather Condition'}) #renamed for this command only


# In[39]:


data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True) #done


# In[42]:


# Finding the mean value of 'Visibility'


# In[43]:


data.Visibility_km.mean()#answer


# In[44]:


#Finding the Standard deviation of "Pressure"


# In[46]:


data.Press_kPa.std() #answer


# In[47]:


#Finding the Variance of "Relative Humidity"


# In[48]:


data['Rel Hum_%'].var() #answer


# In[57]:


#Finding all instances when 'Snow' was recorded


# In[58]:


#value_counts()
data['Weather Condition'].value_counts()


# In[69]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[72]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')].head(50)


# In[73]:


#Finding all instances when "Wind Speed is above 24" and "Visibility is 25"


# In[75]:


data[(data['Wind Speed_km/h'] >24) & (data['Visibility_km'] == 25)]


# In[77]:


#Finding the mean value of each column against each 'Weather Condition'


# In[78]:


data.groupby('Weather Condition').mean()


# In[ ]:




