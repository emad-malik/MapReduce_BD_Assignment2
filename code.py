# importing relevant libraries
import numpy as np
import pandas as pd
import seaborn as sns
import string
# reading file
wikimedia_data= pd.read_csv('filename.csv')
# wikimedia_data.head()
# this fucntion removes punctuation marks from the section text
def remove_punctuation(text):
    # iterate over each punctuation mark in string.punctuation
    for punctuation_mark in string.punctuation:
        text= text.replace(punctuation_mark, '')
    return text
def remove_pucntuation_sectiontext(dataframe, column_name= 'section_text'):
    # Apply the remove_punctuation function to each entry in the specified column
    dataframe[column_name]= dataframe[column_name].apply(remove_punctuation)
    return dataframe
# this function removes stopwords from section text
def remove_stopwords_sectiontext(dataframe, column_name= 'section_text'):
    stopwords= set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
    # using lambda function to filter text
    dataframe[column_name]= dataframe[column_name].apply(lambda text: ' '.join([word for word in text.split() if word.lower() not in stopwords]))
    return dataframe
# call functions to clean text
filtered_text= remove_pucntuation_sectiontext(wikimedia_data, 'section_text')
filtered_text= remove_stopwords_sectiontext(wikimedia_data, 'section_text')



