from __future__ import division

class PR:
# expect data to be list of Boolean value
  def __init__(self, data, total_matches):
    self.data = data
    self.total = total_matches
    self.N = len(data)
    self.matches_found = data.count(True)

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

  def map_score(self):
    total_p = 0
    for n in range(self.N):
      if self.data[n]:
        total_p += self.precision(n+1)
    return total_p/self.matches_found

  def f_score(self, n):
    p = self.precision(n)
    r = self.recall(n)
    return 2*p*r/(p+r)
