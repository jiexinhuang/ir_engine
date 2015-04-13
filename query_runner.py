import pickle

query_pkl = open('query.pkl', 'rb')
queries = pickle.load(query_pkl)

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)

posting_pkl = open('posting.pkl', 'rb')
posting = pickle.load(posting_pkl)

idf_pkl = open('idf.pkl', 'rb')
idf = pickle.load(idf_pkl)

query_pkl.close()
qrel_pkl.close()
posting_pkl.close()
idf_pkl.close()
