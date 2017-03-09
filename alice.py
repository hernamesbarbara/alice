#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""alice.py
"""
from string import punctuation
import nltk
# set stopwords to the built in list from nltk
# check for them in your count_words func to rm stop words w/ little lexical diversity

try:
    from nltk.corpus import stopwords
    STOP_WORDS = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    STOP_WORDS = set(stopwords.words('english'))

def count_words(txt_or_file):
    try:
        txt = open(txt_or_file,"r").read()
    except IOError:
        txt = txt_or_file
    txt = "".join(ch for ch in txt if ch not in punctuation).lower()
    wc = {}
    for word in txt.split():
        if word not in STOP_WORDS:
            if word not in wc:
                wc[word] = 1
            else:
                wc[word] += 1
    return sorted(wc.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    alice_words = count_words("alice.txt")
    for word, cnt in alice_words:
        print "{} => {}".format(word, cnt)

