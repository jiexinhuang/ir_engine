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
    words = tokenizer.tokenize(text)
    words = map(lowercase, words)
    words = map(stemming, words)
    words = filter(stopping, words)
    return FreqDist(words)

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
