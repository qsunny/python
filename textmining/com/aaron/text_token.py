import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# sample text for performing tokenization


def print_text_tokenize(text):
    # Passing the string text into word tokenize for breaking the sentences
    token = word_tokenize(text)
    print(token)
    return token

def print_text_sentence_tokenization(text):
    sentence_tokenized_text = sent_tokenize(text)
    print(sentence_tokenized_text)
    fdist = FreqDist(sentence_tokenized_text)
    print(fdist)
    print(fdist.most_common(2))

    # fdist.plot(30, cumulative=False)
    # plt.show()


if __name__ == "__main__":
    text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern \
    side of South America"
    text = "Download individual packages from http://nltk.org/nltk_data/ (see the “download” links). Unzip them \
    to the appropriate subfolder. For example"
    token = print_text_tokenize(text)
    tokenized_sent = set(stopwords.words("english"))
    print(tokenized_sent)

    filtered_sent = []
    for w in tokenized_sent:
        if w not in tokenized_sent:
            filtered_sent.append(w)
    print("Tokenized Sentence:", tokenized_sent)
    print("Filterd Sentence:", filtered_sent)

    ps = PorterStemmer()
    stemmed_words = []
    for w in filtered_sent:
        stemmed_words.append(ps.stem(w))

    print("Filtered Sentence:", filtered_sent)
    print("Stemmed Sentence:", stemmed_words)

    lem = WordNetLemmatizer()
    stem = PorterStemmer()
    word = "flying"
    print("Lemmatized Word:", lem.lemmatize(word, "v"))
    print("Stemmed Word:", stem.stem(word))


    text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
    The sky is pinkish-blue. You shouldn't eat cardboard"""
    print_text_sentence_tokenization(text)

    sent = "Albert Einstein was born in Ulm, Germany in 1879."
    tokens = nltk.word_tokenize(sent)
    print(tokens)
    print(nltk.pos_tag(tokens))
