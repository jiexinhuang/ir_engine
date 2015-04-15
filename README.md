##Information Retrieval Engine User's Guide

###Dependencies:

Python 2.7, with the following third party packages:
* nltk.corpus
* nltk.tokenize
* nltk.stem
* nltk.corpus
* nltk.probability
* matbpltlib


Get started:
* You should have extracted this archive when you read this.
* copy proj1data.zip to the project root directory
* unzip proj1data.zip.
* (optional)preprocess the corpus, with 
    `python preprocessing.py`
  proprocessed file in pickle format is already included in this package, with default settings in config.json. It is OK to skip this step if using the engine with default settings.
  This step is relatively slow, depending on speed of computer. However, turn off phrase_query support will accelerate this process significantly.
* Default settings has phrase_query switched on 
* More corpus could be added under blogs directory

Configuration:
modify config.json to change strategies used by the engine.
config.json need to be valid JSON document.
Note each time config.json is updated, you will need to preprocess the corpus again, so that the engine could work properly.

API:
in python script of interactive shell
```
import engine

# Create new Engine instance
eg = engine.Engine()

# Search by words
eg.search('query terms string goes here', 100)

# Search by phrase(if switched on)
eg.phrase_search('query phrase, quoting is not neccessary', 20)
```

second parameter of search and phrase_search is the max number of results returned
