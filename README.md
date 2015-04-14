# Project 1: Implementation of Information Retrieving Engine

## Overview
This project implemented a basic Information Retrieval engine which allows user to query for related blog documents with a term.
extension implemented: Phrase search.
## Default Strategies

- For each document


## Performance Measureing

for queries that qrels is availabe, assume all related documents are listed in qrels. So it is easy to get total number of matched documents.
Pooling is not required to calculate recall in this case.

## Query quality Tuning:

As there are so many combination of choices. It is not feasible to test the quality for all combinations.

Instead, I only change one factor of the default setting, and compare the result(listed above)

Normalize document length or not?

diffrent tf weighting

Stemming first or stopping first

Generally performance tuning is all about compromise. We either trade space for speed or trade spped for space.

In large scale dataset, these observations might be very different.


## Index storage and loading time optimization

The engine compare similarity of query and documents with the cosine distance of their term vectors.
However, it is not efficient to store the term vector for each document.
So Inverted index of each term is stored instead.

- Initialy, store normalized term weight `df*idf` directly in posting list, long float number

term      | list
'kid'     | {'BLOG06-20060207-023-0034160690': 0.023427492832506086, 'BLOG06-20060221-017-0014443773': 0.027692438781085564}

pickle file size about 172M Bytes

- Float number cost more space to store Store integer value of frequency only. Store idf and file normalized length individually, caldulate `df*idf` when running queries.
term      | list
'kid'     | {'BLOG06-20060207-023-0034160690': 1, 'BLOG06-20060221-017-0014443773': 1 }

- Try avoid save document_id as long stream?
Use index of document as id
extra storage required for index from id to real document name

For each term, a list of documents that contains this term is stored.
For word queries, document id and term frequency in the document.
For phrase queries, as positional index is used, must also store all positional index of the term in document.
As in memory index is used in the project, Hash table is a reasonable way to store the index.
Where term is the key, documents info is the value

For this particular corpus, after stemming and stopping, a vocabulary of 230637 is generated from the corpus.

Benifit of hash table:
the average cost of each lookup is independent fo the table size.
In Python, it is implemented as a built-in data type: dictionary.
Persistent storage of processed data through pickle

Storage scalability analysis

For large dataset, in memory index is not feasible, so dedicated database is used.
Documents are loosely coupled, no-sql database is the winner in this area.
Popular options including Redis MongoDB.
Also as each term entry is independant, it is easy to distribute them on different clusters with smaller subsets,
Query each set in parralel and generate final result at last. (Google MapReduce)


Engine configuration is stored in config.json 

    options       |   Description
 ------------     |   -------------    
  blogs_root      |   directory for corpus
  stopping        |   Whether to remove stopping words
  stemming        |   Whether to use word stemming (PorterStemmer used)
  lemmatization   |   Whether to use lemmatizer on words (WordNetLemmatizer used)
  max_result      |   Max numbers of results returned by engine

