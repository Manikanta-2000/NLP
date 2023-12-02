#!/usr/bin/env python
# coding: utf-8

# # Extractive Text Summarization 

# In[ ]:

#References - 1)https://stackabuse.com/text-summarization-with-nltk-in-python/

#2)https://www.mygreatlearning.com/blog/text-summarization-in-python/ From the above pages logic has been build for exractive text summarization

#https://www.kaggle.com/code/vshantam/text-summarization-extractive-bleu/input From the above link articles and their summaries were taken for validation The folder BBC News Summary was donwloaded from above link



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
import nltk

def bleu_score(generated_summary,actual_summary):
    hypothesis = generated_summary
    reference = actual_summary
    BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
    return BLEUscore


# In[13]:


def process_summarization(text):
    sentences=tokenize_sentences(text)
    updated_sentences = remove_stopwords(sentences)
    all_tokens = generate_tokens(updated_sentences)
    wordfrequencies = word_frequency(all_tokens)
    weighted_frequencies = weighted_frequency(wordfrequencies)
    sentence_weighted_frequency = sentence_frequency(sentences,weighted_frequencies)
    thresholdFrequency = threshold_frequency(sentence_weighted_frequency)
    generated_summary = final_summary(sentence_weighted_frequency,thresholdFrequency)
    return generated_summary


# In[14]:


file1=open("./BBC News Summary/BBC News Summary/News Articles/entertainment/001.txt","r+")
text=file1.read()
file1.close()
generated_summary=process_summarization(text)


# In[15]:


generated_summary


# In[16]:


summarized_file=open("./BBC News Summary/BBC News Summary/Summaries/entertainment/001.txt","r+")
actual_summary=summarized_file.read()
summarized_file.close()


# In[17]:


actual_summary


# In[18]:


print("BLEU_Score : ",bleu_score(generated_summary,actual_summary))


# In[19]:


file1=open("./BBC News Summary/BBC News Summary/News Articles/tech/100.txt","r+")
text=file1.read()
file1.close()


# In[20]:


generated_summary=process_summarization(text)


# In[21]:


generated_summary


# In[22]:


summarized_file=open("./BBC News Summary/BBC News Summary/Summaries/tech/100.txt","r+")
actual_summary=summarized_file.read()
summarized_file.close()


# In[23]:


actual_summary


# In[24]:


print("BLEU_Score : ",bleu_score(generated_summary,actual_summary))





