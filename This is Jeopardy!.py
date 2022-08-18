#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_colwidth', None)


# In[2]:


jeopardy = pd.read_csv('jeopardy.csv')


# In[3]:


jeopardy


# In[4]:


# First check the format of column's title
jeopardy.columns


# In[5]:


# Except the title 'Show Number', the rest is not correct because they all have unnecessary space


# In[6]:


# Reformatting the name of columns

jeopardy = jeopardy.rename(columns={' Air Date':'Air Date',' Round':'Round',' Category':'Category',
                         ' Value':'Value',' Question':'Question',' Answer':'Answer'})
jeopardy.columns


# In[7]:


jeopardy['Question']


# In[8]:


# Find the questions contain the word 'leader' or 'Leader'
# The index present the ID number of question

index = 0
list_of_words = [' leader ',' Leader ',' leaders ',' Leaders ']

for string in jeopardy['Question']:
    for word in list_of_words:
        if word in string:
            print(str(index) + ': '+ string)
            print(' ')
        else: continue
        
    index+=1    


# In[9]:


# 'In order to convert string value 'None' into float type, firstly convert it into string of number type

jeopardy['Value']=jeopardy['Value'].apply(lambda value: '0' if value == 'None' else value)
jeopardy


# In[10]:


# Calculate the mean of some particular rows

float_value = []

for value in jeopardy['Value']:
    value = value.strip('$')
    value = value.replace(',','')
    value = float(value)
    value = round(value,0)
    float_value.append(value)
    
float_value


# In[11]:


# Add new column of float value into dataset

dataframe = pd.DataFrame(jeopardy)
dataframe.insert(7,'Float Value',float_value)


# In[12]:


jeopardy


# In[13]:


list_of_words = [' leader ',' Leader ']

# in orer to avoid the words in list become a subtring of other phrases, we should put head space and tail space for each value in list
# The following function is written that find the average price of a set of questions containing a special word 
# or a list of special words

def keyword_mean_values(list_of_words):
    index=0
    counter=0
    sum_value=0
    for string in jeopardy['Question']:
        for word in list_of_words:
            if word in string:
                sum_value+=float_value[index]
                counter+=1
            else: counter+=0    
        index+=1
    mean_value=sum_value/counter
    return mean_value


# In[14]:


# you can change list_of_words to see another result

keyword_mean_values(list_of_words)


# In[15]:


answers=[]
for ans in jeopardy['Answer']:
    answers.append(ans)
answers


# In[16]:


# This code block calculate the number of unique answers for a special keyword and a special list of keywords and present them

def keyword_unique_answer(list_of_words):
    unique_answers=[]
    index=0
    for string in jeopardy['Question']:
        for word in list_of_words:
            if word in string:
                if answers[index] not in unique_answers:
                    unique_answers.append(answers[index])
                else: continue
        index+=1
        
    print('There are total '+ str(len(unique_answers)) +' unique answers for the questions with these keywords!')
    print('')
    print('They are here:')
    return unique_answers


# In[17]:


keyword_unique_answer(list_of_words)


# In[18]:


# we can explore mord interesting things for this jeopardy game, example we can find the frequency of word 'computer'
# between Date in 20s years and 19s year

# First we create two dataframe for date in 20s years and date in 19s years

date_20s = jeopardy[jeopardy['Air Date']>'1999-12-31']
date_19s = jeopardy[(jeopardy['Air Date']>'1899-12-31')&(jeopardy['Air Date']<'1999-12-31')]


# In[19]:


# Next, filtering the questions contain the words relating to 'computer'

computer_in_20s = date_20s[date_20s['Question'].str.contains('computer'or'computers'or'Computer'or'Computers')]
len(computer_in_20s)


# In[ ]:


computer_in_19s = date_19s[date_19s['Question'].str.contains('computer'or'computers'or'Computer'or'Computers')]
len(computer_in_19s)


# In[ ]:


# we can see the frequency of word 'computer' in 20s years is higher than in 19s years
# Morever, we can analyze more interesting things and expand your knowledge

