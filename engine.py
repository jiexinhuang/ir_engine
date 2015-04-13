from __future__ import division
import pickle
from text_processor import process
from math import log
from math import sqrt

class Engine:
    def __init__(self, result_length):
        self.result_length = result_length
        # Load all pkl files into memery to indexing
        posting_pkl = open('posting.pkl', 'rb')
        self.posting = pickle.load(posting_pkl)

        idf_pkl = open('idf.pkl', 'rb')
        self.idfs = pickle.load(idf_pkl)
        self.N = len(self.idfs)

        file_length_pkl = open('file_length.pkl', 'rb')
        self.file_length = pickle.load(file_length_pkl)

        posting_pkl.close()
        idf_pkl.close()
        file_length_pkl.close()

    def search(self, query):
        result = {}
        terms = process(query)
        for term, qtf in terms.iteritems():
            if self.idfs.has_key(term):
                idft = log(self.N/self.idfs[term])
                for document, dft in self.posting[term].iteritems():
                    normalization = sqrt(self.file_length[document])
                    dft = dft/normalization
                    if result.has_key(document):
                        result[document] += dft*idft
                    else:
                        result[document] = dft*idft
        return [ (doc, result[doc]) for doc in sorted(result, key=result.get, reverse=True)]
