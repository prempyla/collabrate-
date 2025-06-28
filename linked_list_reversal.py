'''
    {
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
def reverseLL(head):
    prev = None
    current = head

    while current:
        next_node = current.next 
        current.next = prev      
        prev = current        
        current = next_node   

    return prev
