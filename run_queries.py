import pickle
from engine import Engine

query_pkl = open('query.pkl', 'rb')
queries = pickle.load(query_pkl)
query_pkl.close()

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)
qrel_pkl.close()

engine = Engine()

query_eval = {}

for query_id, terms in queries.iteritems():
  result = engine.search(terms)
  docs = [ doc for doc, score in result ]
  qrel = qrels[query_id]
  evaluation = [ doc in qrel for doc in docs ]
  query_eval[query_id] = evaluation


eval_pickle = open('queries_eval.pkl', 'wb')
pickle.dump(query_eval, eval_pickle)

eval_pickle.close()
