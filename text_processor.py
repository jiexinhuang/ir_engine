# Given a document, return a bag of words
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.probability import FreqDist 
from config import settings

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stops = stopwords.words('english')

def process(text):
    return FreqDist(raw_process(text))

def raw_process(text):
    words = tokenizer.tokenize(text)
    words = map(lowercase, words)
    if settings['stemming']:
      words = map(stemming, words)
    if settings['lemmatization']:
      words = map(lemmatize, words)
    if settings['stopping']:
        words = filter(stopping, words)
    return words

def stopping(word):
    return len(word) > 1 and word not in stops

def stemming(word):
    return stemmer.stem(word)

def lowercase(word):
    return word.lower()

def lemmatize(word):
    return lemmatizer.lemmatize(word)

def normalization(values):
    return reduce(lambda x, y: x+y*y, values)
