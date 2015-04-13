# Create bag of words representation of documents
from __future__ import division
from math import log
from math import sqrt
from nltk.corpus import PlaintextCorpusReader
from text_processor import process
import pickle

class Documents:
    def __init__(self, root):
        self.files = PlaintextCorpusReader(root, '.*\.txt')
        self.posting = {}
        self.idf = {}
        self.N = len(self.files.fileids())

    def process(self):
        for file in self.files.fileids():
            text = self.files.raw(file)
            words = process(text)
            if words.values():
                normalization = sqrt(reduce(lambda x, y: x+y*y, words.values()))
            for word, freq in words.iteritems():
                if self.idf.has_key(word):
                    self.idf[word] += 1
                else:
                    self.idf[word]  = 1

                if not self.posting.has_key(word):
                    self.posting[word] = {}
                self.posting[word][file] = freq/normalization
        self.idf = { term: log(self.N/dft) for term, dft in self.idf.iteritems() }

    def dump(self):
        posting_pickle = open('posting.pkl', 'wb')
        pickle.dump(self.posting, posting_pickle)
        posting_pickle.close()

        idf_pickle = open('idf.pkl', 'wb')
        pickle.dump(self.idf, idf_pickle)
        idf_pickle.close()
