#!/usr/bin/env python
# coding: utf-8

# # Extractive Text Summarization 

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import re


# In[2]:


#splits the texts in to sentences
pattern = r'[.!?\n]+'
def tokenize_sentences(text):
    sentences = re.split(pattern,text)
    while ("" in sentences):
        sentences.remove("")
    while(" " in sentences):
        sentences.remove(" ")
    return sentences


# In[4]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[5]:


def remove_stopwords(sentences):
    stop_words= set(stopwords.words('english'))
    updated_sentences = []
    for i in sentences:
        words = word_tokenize(i)
        cleaned_words = [word for word in words if word.lower() not in stop_words and word.isalpha()]
        cleaned_sentence = ' '.join(cleaned_words)
        updated_sentences.append(cleaned_sentence)
    return updated_sentences


# In[6]:


def generate_tokens(sentences):
    all_tokens=[]
    for i in sentences:
        all_tokens.extend(i.split(" "))
    return all_tokens


# In[7]:


from collections import OrderedDict
def word_frequency(all_tokens):
    wordfrequencies = OrderedDict()
    for i in all_tokens:
        if i.lower() not in wordfrequencies:
            wordfrequencies[i.lower()] = 1
        else:
            wordfrequencies[i.lower()]+=1
    return wordfrequencies


# In[8]:


from collections import OrderedDict
def weighted_frequency(wordfrequencies):
    max_frequency = max(wordfrequencies.values())
    weighted_frequencies = OrderedDict()
    for i in wordfrequencies:
        weighted_frequencies[i] = wordfrequencies[i]/max_frequency
    return weighted_frequencies


# In[9]:


from collections import OrderedDict
def sentence_frequency(sentences,weighted_frequencies):
    sentence_weighted_frequency = OrderedDict()
    pattern = r'[!\"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~\s]+'
    for i in sentences:
        weighted_frequency = 0
        split_words = re.split(pattern,i)
        for j in split_words:
            if j.lower() not in weighted_frequencies:
                weighted_frequency+=0
            else:
                weighted_frequency+=weighted_frequencies[j.lower()]
        sentence_weighted_frequency[i]=weighted_frequency
    return sentence_weighted_frequency


# In[10]:


def threshold_frequency(sentence_weighted_frequency):
    frequency_sum = sum(sentence_weighted_frequency.values())
    length = len(sentence_weighted_frequency)
    thresholdFrequency = frequency_sum/length
    return thresholdFrequency


# In[11]:


def final_summary(sentence_weighted_frequency,thresholdFrequency):
    summary=""
    for i in sentence_weighted_frequency:
        if sentence_weighted_frequency[i]>=thresholdFrequency:
            if summary:
                summary=summary+". "+i
            else:
                summary=summary+i
    summary = summary+"."
    return summary


# In[12]:





# In[ ]:




