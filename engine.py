from __future__ import division
import cPickle as pickle
from text_processor import process
from config import settings
from math import log
from math import sqrt

class Engine:
    def __init__(self):
        # Load all pkl files into memery to indexing
        posting_pkl = open('posting.pkl', 'rb')
        self.posting = pickle.load(posting_pkl)

        ids_pkl = open('file_ids.pkl', 'rb')
        self.id_names = pickle.load(ids_pkl)

        self.N = len(self.posting)

        file_length_pkl = open('file_length.pkl', 'rb')
        self.file_length = pickle.load(file_length_pkl)

        ids_pkl.close()
        posting_pkl.close()
        file_length_pkl.close()

    def search(self, query, k):
        result = {}
        terms = process(query)
        for term, qtf in terms.iteritems():
            if self.posting.has_key(term):
                doc_list = eval(self.posting[term])
                idft = log(self.N/(doc_list.pop('idf')))
                for document, dft in doc_list.iteritems():
                    normalization = sqrt(self.file_length[document])
                    if settings['phrase_query']:
                        dft = len(dft)
                    dft = dft/normalization
                    if result.has_key(document):
                        result[document] += dft*idft
                    else:
                        result[document] = dft*idft
        result_ids = sorted(result, key=result.get, reverse=True)[0:k]
        return [self.id_names[idx] for idx in result_ids]
