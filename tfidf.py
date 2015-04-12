from __future__ import division
import tokenizer
import math

documents = tokenizer.bag_of_words

idf = {}

N = len(documents)

for document, words in documents.iteritems():
  for word, freq in words.iteritems():
    if idf.has_key(word):
      idf[word] += freq
    else:
      idf[word]  = freq

idf = { term: math.log(N/dft) for term, dft in idf.iteritems() }
