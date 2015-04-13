import pickle
from query_runner import QueryRunner

query_pkl = open('query.pkl', 'rb')
queries = pickle.load(query_pkl)
query_pkl.close()

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)
qrel_pkl.close()
