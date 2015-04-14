# Create bag of words representation of documents
from __future__ import division
from nltk.corpus import PlaintextCorpusReader
from text_processor import raw_process
from text_processor import process
from text_processor import normalization
from config import settings
import cPickle as pickle

def indices(li, elem):
    return [i for i, x in enumerate(li) if x == elem]

class Documents:
    def __init__(self, root):
        self.files = PlaintextCorpusReader(root, '.*\.txt')
        self.posting = {}
        self.idf = {}
        self.file_length = {}
        self.file_id_names = {}
        self.N = len(self.files.fileids())

    def process(self):
        for idx, file in enumerate(self.files.fileids()):
            print idx
            filename = file.strip('.txt')
            self.file_id_names[idx] = filename
            text = self.files.raw(file)
            words = process(text)
            if settings['phrase_query']:
                raw_words = raw_process(text)
            if words.values():
                self.file_length[idx] = normalization(words.values())
            for word, freq in words.iteritems():
                if self.idf.has_key(word):
                    self.idf[word] += 1
                else:
                    self.idf[word]  = 1

                if not self.posting.has_key(word):
                    self.posting[word] = {}
                if settings['phrase_query']:
                    self.posting[word][idx] = indices(raw_words, word)
                else:
                    self.posting[word][idx] = freq
        for word, idf in self.idf.iteritems():
            self.posting[word]['idf'] = idf

    def dump(self):
        posting_pickle = open('posting.pkl', 'wb')
        for term, value in self.posting.iteritems():
          self.posting[term] = str(value)
        pickle.dump(self.posting, posting_pickle, 2)
        posting_pickle.close()

        length_pickle = open('file_length.pkl', 'wb')
        pickle.dump(self.file_length, length_pickle, 2)
        length_pickle.close()

        file_ids_pickle = open('file_ids.pkl', 'wb')
        pickle.dump(self.file_id_names, file_ids_pickle, 2)
        file_ids_pickle.close()
