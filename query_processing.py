import re
import cPickle as pickle

query_file = open('06.topics.851-900.txt', 'r').read().split('<top>')

queries = {}

for query in query_file:
    lines = query.split('\n')
    key = None
    value = None
    for line in lines:
        number = re.search('<num>\D+(\d+)', line)
        title = re.search('<title>(.+)', line)
        if number:
            key = number.group(1)
        if title:
            value = title.group(1).strip()
    if key:
        queries[int(key)] = value

query_pickle = open('query.pkl', 'wb')
pickle.dump(queries, query_pickle, 2)

query_pickle.close()


# process qrels.february to get related documents for each query
qrel_file = open('qrels.february', 'r')

relations = {}

for line in qrel_file:
    line = line.strip().split()
    if line[3] != '0':
        query_id = int(line[0])
        document_id = line[2]
        if relations.has_key(query_id):
            relations[query_id].append(document_id)
        else:
            relations[query_id] = [document_id]

qrel_pickle = open('qrel.pkl', 'wb')
pickle.dump(relations, qrel_pickle, 2)

qrel_pickle.close()
