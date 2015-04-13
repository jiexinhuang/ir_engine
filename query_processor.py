import re
import pickle

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
        queries[key] = value

query_pickle = open('query.pkl', 'wb')

pickle.dump(queries, query_pickle)

query_pickle.close()
