class Node():
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

class Stack():
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self) -> bool:
        return self.head == None
    
    def push(self, data) -> None:
        new_head = Node(data, self.head)
        self.head = new_head
        
    def pop(self) -> int:
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
        
            return data
        else:
            
            return None
    
    def get_elements(self) -> list:
        curr_node = self.head
        
        nodes_data = []
        while curr_node != None:
            nodes_data.append(str(curr_node.data))
            curr_node = curr_node.next
            
        return nodes_data
    
    
if __name__ == '__main__':
    stack = Stack()
    
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
    