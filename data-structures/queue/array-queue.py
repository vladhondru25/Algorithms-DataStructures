class Queue():
    def __init__(self, capacity) -> None:
        self.head = 0
        self.tail = 0
        self.count = 0
        
        self.array_queue = [None] * capacity
        
    def is_empty(self) -> bool:
        return self.count == 0
    
    def is_full(self) -> bool:
        return self.count == len(self.array_queue)
    
    def enque(self, data) -> None:
        self.array_queue[self.tail] = data
        self.tail = (self.tail + 1) % len(self.array_queue)
            
        if self.is_full():
            self.head = (self.head + 1) % len(self.array_queue)
        else:
            self.count += 1
        
        
    def deque(self) -> int:
        if not self.is_empty():
            data = self.array_queue[self.head]
            self.array_queue[self.head] = None
            
            self.head = (self.head + 1) % len(self.array_queue)
        
            self.count -= 1
        
            return data
        else:
            return None
    
    def get_elements(self) -> list:
        if self.is_empty():
            return []

        nodes_data = []
        if self.head < self.tail:
            for e in self.array_queue[self.head:self.tail]:
                nodes_data.append(str(e))
        else:
            for i in range(self.head,self.tail+len(self.array_queue)):
                e = self.array_queue[i%len(self.array_queue)]
                nodes_data.append(str(e))
            
        return nodes_data
    
    
if __name__ == '__main__':
    stack = Queue(capacity=3)
    
    stack.enque(1)
    stack.enque(2)
    nodes_data = stack.get_elements()
    assert nodes_data == ['1', '2']
    print('->'.join(nodes_data))
    
    stack.enque(4)
    stack.deque()
    stack.enque(3)
    stack.deque()
    nodes_data = stack.get_elements()
    assert nodes_data == ['4', '3']
    print('->'.join(nodes_data))
    
    stack.deque()
    stack.deque()
    stack.deque()
    
    nodes_data = stack.get_elements()
    assert nodes_data == []
    print('->'.join(nodes_data))
    