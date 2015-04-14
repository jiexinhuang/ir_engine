# Project 1: Implementation of Information Retrieving Engine

## Overview

This project implemented a basic Information Retrieval engine which allows 

## Performance Measureing

for queries that qrels is availabe, assume all related documents are listed in qrels. So it is easy to get total number of matched documents.
Pooling is not required to calculate recall in this case.

## Performance Tuning:

Compare these factors

Normalize document length or not?

diffrent tf weighting


Generally performance tuning is all about compromise. We either trade space for speed or trade spped for space.

In large scale dataset, these observations might be very different.


## Index storage optimization

When query and documents are compared with cosine distance

Python dictionary type(Essentially Hash Table in memory)

After stemming and stopping, a vocabulary of 230637 is generated from the corpus.

- Stemming first or stopping first

Index Data stucture

inverted index



Engine configuration is stored in config.json 

    options       |   Description
 ------------     |   -------------    
  stopping        |   Whether to remove stopping words
  stemming        |   Whether to use word stemming (PorterStemmer used)
  lemmatization   |   Whether to use lemmatizer on words (WordNetLemmatizer used)
  max_result      |   Max numbers of results returned by engine


