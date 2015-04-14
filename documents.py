# Create bag of words representation of documents
from __future__ import division
from nltk.corpus import PlaintextCorpusReader
from text_processor import process
from text_processor import normalization
import cPickle as pickle

class Documents:
    def __init__(self, root):
        self.files = PlaintextCorpusReader(root, '.*\.txt')
        self.posting = {}
        self.idf = {}
        self.file_length = {}
        self.N = len(self.files.fileids())

    def process(self):
        for idx, file in enumerate(self.files.fileids()):
            filename = file.strip('.txt')
            text = self.files.raw(file)
            words = process(text)
            if words.values():
                self.file_length[idx] = normalization(words.values())
            for word, freq in words.iteritems():
                if self.idf.has_key(word):
                    self.idf[word] += 1
                else:
                    self.idf[word]  = 1

                if not self.posting.has_key(word):
                    self.posting[word] = {}
                self.posting[word][idx] = freq
        # self.idf = { term: log(self.N/dft) for term, dft in self.idf.iteritems() }

    def dump(self):
        posting_pickle = open('posting.pkl', 'wb')
        pickle.dump(self.posting, posting_pickle, 2)
        posting_pickle.close()

        idf_pickle = open('idf.pkl', 'wb')
        pickle.dump(self.idf, idf_pickle, 2)
        idf_pickle.close()

        length_pickle = open('file_length.pkl', 'wb')
        pickle.dump(self.file_length, length_pickle, 2)
        length_pickle.close()
