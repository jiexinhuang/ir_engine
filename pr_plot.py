from __future__ import division
import pickle
import matplotlib.pyplot as plt

eval_pkl = open('queries_eval.pkl', 'rb')
evaluation = pickle.load(eval_pkl)
eval_pkl.close()

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)
qrel_pkl.close()

class PR:
# expect data to be list of Boolean value
  def __init__(self, data, total_matches):
    self.data = data
    self.total = total_matches
    self.N = len(data)

  def precision(self, n):
    return self.matches(n)/n

  def recall(self, n):
    return self.matches(n)/self.total

  def matches(self, n):
    return self.data[0:n].count(True)

  def precision_list(self):
    return [ self.precision(n) for n in range(1, self.N) ]

  def recall_list(self):
    return [ self.recall(n) for n in range(1, self.N) ]

  def f_score(self, n):
    p = self.precision(n)
    r = self.recall(n)
    return 2*p*r/(p+r)


pr = PR(evaluation[851], len(qrels[851]))

# plt.plot(pr.recall_list(), pr.precision_list())
# plt.show()
