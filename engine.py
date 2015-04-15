from __future__ import division
import cPickle as pickle
from text_processor import process
from text_processor import raw_process
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

    def phrase_search(self, query, k):
        if self.valid_phrase(query):
            self.term_lists = {}
            result_ids = []
            terms = raw_process(query)
            head, tail = terms[0], terms[1:]

            for term in tail:
                term_list = eval(self.posting[term])
                term_list.pop('idf')
                self.term_lists[term] = term_list

            head_list = eval(self.posting[head])
            head_list.pop('idf')
            for doc_id, positions in head_list.iteritems():
                for position in positions:
                    if self.match_tail(tail, doc_id, position):
                        result_ids.append(doc_id)
                        break

            word_search_result = self.search(query, None)
            unsorted_result = [self.id_names[idx] for idx in result_ids]
            result = []

            for doc_name in word_search_result:
                if doc_name in unsorted_result:
                    result.append(doc_name)
            return result[0:k]
        else:
            return []

    # check more than one word in term
    # check all terms in dictionary before do phrase search
    def valid_phrase(self, query):
        dictionary = self.posting.keys()
        terms = raw_process(query)
        terms_in_dic = [ term in dictionary for term in terms]
        all_terms_in_dic = reduce(lambda a, b: a and b, terms_in_dic, True)
        return len(terms)>1 and all_terms_in_dic
            
    def match_tail(self, tail, doc_id, position):
        matching_flag = True
        for idx, term in enumerate(tail):
            term_list = self.term_lists[term]
            if term_list.has_key(doc_id):
                term_positions = term_list[doc_id]
                if (position+idx+1) not in term_positions:
                    matching_flag = False
            else:
                matching_flag = False
        return matching_flag
