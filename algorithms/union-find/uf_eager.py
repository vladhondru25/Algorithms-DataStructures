class QuickFindUF:
    def __init__(self, n: int) -> None:
        self.id = list(range(n))
        
    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]
    
    def union(self, p: int, q: int) -> None:
        if self.connected(p,q):
            return
        
        pid = self.id[p]
        qid = self.id[q]
        
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
        
        
if __name__ == '__main__':
    uf = QuickFindUF(10)
    
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    
    assert uf.connected(0, 7) == False
    assert uf.connected(8, 9) == True
    
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(1, 0)
    
    assert uf.connected(0, 7) == True
    
    print('Correct!')