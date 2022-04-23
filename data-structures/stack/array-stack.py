class Stack():
    def __init__(self, capacity) -> None:
        self.n = 0
        self.stack_array = [None] * capacity
        
    def is_empty(self) -> bool:
        return self.n == 0
    
    def push(self, data) -> None:
        if self.n == len(self.stack_array):
            self.resize(len(self.stack_array))
            
        self.stack_array[self.n] = data
        self.n += 1
        
    def pop(self) -> int:
        if not self.is_empty():
            data = self.stack_array[self.n]
            self.stack_array[self.n] = None
            self.n -= 1
        
            return data
        else:
            return None
    
    def get_elements(self) -> list:
        nodes_data = []
        for i in range(self.n-1, -1, -1):
            nodes_data.append(str(self.stack_array[i]))
            
        return nodes_data
    
    def resize(self, capacity):
        self.stack_array.extend([None] * capacity)
    
    
if __name__ == '__main__':
    stack = Stack(capacity=2)
    
    stack.push(1)
    stack.push(2)
    nodes_data = stack.get_elements()
    assert nodes_data == ['2', '1']
    print('->'.join(nodes_data))
    
    stack.push(4)
    stack.pop()
    stack.push(3)
    stack.pop()
    nodes_data = stack.get_elements()
    assert nodes_data == ['2', '1']
    print('->'.join(nodes_data))
    
    stack.pop()
    stack.pop()
    stack.pop()
    
    nodes_data = stack.get_elements()
    assert nodes_data == []
    print('->'.join(nodes_data))
    