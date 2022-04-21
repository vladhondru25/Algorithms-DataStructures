class QuickUnionUF:
    def __init__(self, n: int) -> None:
        self.id = list(range(n))
        self.sz = [1] * n
        
    def __root(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
            
        return i
        
    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)
    
    def union(self, p: int, q: int) -> None:
        i = self.__root(p)
        j = self.__root(q)
        
        if i == j:
            return
        
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[i] += self.sz[j]
        else:
            self.id[j] = i
            self.sz[j] += self.sz[i]
        
        
if __name__ == '__main__':
    uf = QuickUnionUF(10)
    
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
    
    print(uf.id)
    
    print('Correct!')