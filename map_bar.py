from __future__ import division
from query_eval import PR
import cPickle as pickle
import matplotlib.pyplot as plt
import sys

eval_pkl = open('queries_eval.pkl', 'rb')
evaluation = pickle.load(eval_pkl)
eval_pkl.close()

qrel_pkl = open('qrel.pkl', 'rb')
qrels = pickle.load(qrel_pkl)
qrel_pkl.close()

id_ranges = range(851, 901)
scores = [ PR(evaluation[query_id], len(qrels[query_id])).map_score() for query_id in id_ranges ]
print sum(scores)/50

plt.plot(id_ranges, scores)
plt.show()

# offset = int(sys.argv[1])

# color_list = ['y', 'm', 'c', 'r', 'g', 'b', 'w', 'k']
# for query_id in range(8):
#   color = color_list[query_id]
#   query_id += offset
#   pr = PR(evaluation[query_id], len(qrels[query_id]))

#   plt.plot(pr.recall_list(), pr.precision_list(), color)
#   plt.xlabel('Recall')
#   plt.ylabel('Precision')

# plt.show()
