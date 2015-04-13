# Create bag of words representation of documents
from __future__ import division
from math import log
from math import sqrt
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist 
import pickle

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

proj_root = '/home/jason/ir_engine/'
document_root = proj_root + 'blogs'

# Use tokenizer to remove puntuations
files = PlaintextCorpusReader(document_root, '.*\.txt')

posting = {}
idf = {}
N = len(files.fileids())

for file in files.fileids():
  text = files.raw(file)
  # convert words to lowercase
  words = map(lowercase, tokenizer.tokenize(text))
  words = filter(stopping, words)
  words = map(stemming, words)
  words = FreqDist(words)
  if words.values():
      file_length_normalization = sqrt(reduce(lambda x, y: x+y*y, words.values()))
  for word, freq in words.iteritems():
    if idf.has_key(word):
      idf[word] += 1
    else:
      idf[word]  = 1

    if not posting.has_key(word):
      posting[word] = {}
    posting[word][file] = freq/file_length_normalization

idf = { term: log(N/dft) for term, dft in idf.iteritems() }


posting_pickle = open('posting.pkl', 'wb')
pickle.dump(posting, posting_pickle)
posting_pickle.close()

idf_pickle = open('idf.pkl', 'wb')
pickle.dump(idf, idf_pickle)
idf_pickle.close()
