#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#Import Data and also encode 


# In[3]:


import pandas as pd

df = pd.read_csv("C:\\Users\\Dell\\Downloads\\E-commerce Sales Analysis1.csv", encoding='latin1')
df


# In[4]:


#Check the columns


# In[5]:


df.columns


# In[6]:


#Checking null values in each columns


# In[7]:


null_values = df.isnull().sum()
null_values


# In[8]:


#Checking the datatype of invoice date


# In[9]:


data_type = df['InvoiceDate'].dtype
data_type


# In[10]:


#Replacing null Values


# In[11]:


df=df.fillna({'Description':'Not available','CustomerID':'0'})
df


# In[12]:


#Checking null Values again


# In[13]:


df.isnull().sum()


# In[14]:


#Checking Data


# In[15]:


df.head()


# In[16]:


#Separating Date and Time from data date column


# In[17]:


df[['Date', 'Time']] = df['InvoiceDate'].str.split(' ', expand=True)


# In[18]:


df.head()


# In[19]:


#Checking Negative Unit price because there are positive data same as that of negative data means orders have been cancelled


# In[20]:


# Assuming df is your DataFrame
Negative_values = df[df['UnitPrice'] < 0]
Negative_values


# In[21]:


#Negative Values for Quantity


# In[22]:


Neg_quantity= df[df['Quantity']<0]
Neg_quantity


# In[23]:


#Same Positive values data as like negative data so we have concluded that the orders are cancelled so need to drop this from data


# In[24]:


p = (df['UnitPrice'] == 11062.06) & (df['Description'] == 'Adjust bad debt')
p= df[p]
p


# In[25]:


#Checking negative values for unit price


# In[26]:


df = df.drop(df[df['UnitPrice'] < 0].index)
df


# In[27]:


df = df.drop(df[df['UnitPrice'] < 0].index)
df


# #Data Processing

# In[28]:


#Calculating revenue


# In[29]:


df['revenue']=df['Quantity']*df['UnitPrice']
df


# In[30]:


#Groupby sum of revenues for countries


# In[31]:


grouped_df = df.groupby('Country')['revenue'].sum().reset_index()
grouped_df


# In[32]:


#Countries with maximum revenue


# In[33]:


df3 = grouped_df.sort_values(by='revenue', ascending=False).head(5)
df3


# In[34]:


import matplotlib.pyplot as plt

# Example data (replace this with your own data)
countries = df3['Country']
revenues = df3['revenue']

# Create a bar plot
plt.bar(countries, revenues, color='blue')
plt.xlabel('Countries')
plt.ylabel('Revenue (in millions)')
plt.title('Revenue by Country')
plt.show()


# In[35]:


#Countries with minimum values


# In[36]:


df4 = grouped_df.sort_values(by='revenue').head(5)
df4


# In[37]:


import matplotlib.pyplot as plt
Countries=df4['Country']
revenues=df4['revenue']
plt.bar(Countries, revenues,color='red')
plt.xlabel('Countries')
plt.ylabel('revenues(in millions)')
plt.title('Countries having minimum revenue')


# In[38]:


df_neg= df[df['revenue']<0]
df_neg


# In[ ]:





# In[39]:


df7=df.groupby('Description')['revenue'].sum().reset_index()
df7


# In[40]:


#Revenue of top 5 products


# In[41]:


dfd=df7.sort_values(by='revenue',ascending=False ).head(5)
dfd


# In[42]:


df_neg= df[df['revenue']<0]
df_neg


# In[43]:


import matplotlib.pyplot as plt
Countries=dfd['Description']
revenues=dfd['revenue']
plt.bar(Countries, revenues,color='green')
plt.xticks(rotation=45, ha='right') 
plt.xlabel('Products')
plt.ylabel('revenues(in millions)')
plt.title('Products having maximum revenue')


# In[48]:


dfc = df7[df7['revenue'] != 0].sort_values(by='revenue').head(5)
dfc


# In[45]:


Countries = dfc['Description']
revenues = dfc['revenue']

# Create a vertical bar plot
plt.bar(Countries, revenues, color='red')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Labeling the axes
plt.xlabel('Products')
plt.ylabel('Revenues (in millions)')

# Adding a title to the plot
plt.title('Products and their Revenues')

# Display the plot
plt.show()


# In[ ]:





# In[46]:


df['Date'] = pd.to_datetime(df['Date'])

# Extract month and date
df['day'] = df['Date'].dt.year


# In[47]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




