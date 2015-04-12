# Create bag of words representation of documents
from __future__ import division
from math import log
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist 
tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stops = stopwords.words('english')

def stopping(word):
  return len(word) > 1 and word not in stops

def stemming(word):
  return stemmer.stem(word)

def lowercase(word):
  return word.lower()

proj_root = '/Users/jiejingdu/Unimelb/ir_proj1/'
document_root = proj_root + 'small'

# Use tokenizer to remove puntuations
files = PlaintextCorpusReader(document_root, '.*\.txt')

bag_of_words = {}
idf = {}
N = len(files.fileids())

for file in files.fileids():
  text = files.raw(file)
  # convert words to lowercase
  words = map(lowercase, tokenizer.tokenize(text))
  words = filter(stopping, words)
  words = map(stemming, words)
  words = FreqDist(words)
  bag_of_words[file] = words
  for word, freq in words.iteritems():
    if idf.has_key(word):
      idf[word] += 1
    else:
      idf[word]  = 1

idf = { term: log(N/dft) for term, dft in idf.iteritems() }
