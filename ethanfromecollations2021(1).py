#!/usr/bin/env python
# coding: utf-8

# In[1]:


import textract

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = (text)
from nltk.tokenize import sent_tokenize, word_tokenize

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = (text)
from nltk.tokenize import sent_tokenize, word_tokenize

import difflib
import nltk
import re

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = text.decode()

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = text.decode()

from nltk.tokenize import sent_tokenize, word_tokenize
from IPython.core.display import HTML

words1 = nltk.word_tokenize(book1)
words2 = nltk.word_tokenize(book2)

htmldiff = difflib.HtmlDiff()
tbl = htmldiff.make_table(words1, words2, context = True)
HTML(tbl) 


# In[3]:


import textract

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = (text)
from nltk.tokenize import sent_tokenize, word_tokenize

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = (text)
from nltk.tokenize import sent_tokenize, word_tokenize

import difflib
import nltk
import re

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = text.decode()

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = text.decode()

from nltk.tokenize import sent_tokenize, word_tokenize
from IPython.core.display import HTML

words1 = nltk.word_tokenize(book1)
words2 = nltk.word_tokenize(book2)

htmldiff = difflib.HtmlDiff()
tbl = htmldiff.make_table(words1, words2)
HTML(tbl) 

