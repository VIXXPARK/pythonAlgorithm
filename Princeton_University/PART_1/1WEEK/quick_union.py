class quick_union:
    def __init__(self,n):
        self._id=list(range(n))
    
    def _root(self,i):
        while i!=self._id[i]:
            i=self._id[i]
        return i
    
    def connected(self,p,q):
        return self._root(p) == self._root(q)
    
    def union(self,p,q):
        i=self._root(p)
        j=self._root(q)
        self._id[i]=j
    
uf = quick_union(10)
for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9),(7, 3), (4, 8), (6, 1)]:
    uf.union(p,q)
print(uf._id)
