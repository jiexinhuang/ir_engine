import pickle
from engine import Engine

query_pkl = open('query.pkl', 'rb')
queries = pickle.load(query_pkl)
query_pkl.close()

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)
qrel_pkl.close()
