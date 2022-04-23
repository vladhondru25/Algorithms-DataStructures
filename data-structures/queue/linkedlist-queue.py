class Node():
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

class Queue():
    def __init__(self) -> None:
        self.firstNode = None
        self.lastNode = None
        
    def is_empty(self) -> bool:
        return self.firstNode == None
    
    def enque(self, data) -> None:
        new_node = Node(data)
        
        if self.is_empty():
            self.lastNode = new_node
            self.firstNode = self.lastNode
        else:  
            self.lastNode.next = new_node
            self.lastNode = new_node
        
    def deque(self) -> int:
        if not self.is_empty():
            data = self.firstNode.data
            self.firstNode = self.firstNode.next
            
            if self.is_empty():
                self.lastNode = None
        
            return data
        else:
            return None
    
    def get_elements(self) -> list:
        curr_node = self.firstNode
        
        nodes_data = []
        while curr_node != None:
            nodes_data.append(str(curr_node.data))
            curr_node = curr_node.next
            
        return nodes_data
    
    
if __name__ == '__main__':
    stack = Queue()
    
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
    