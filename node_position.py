'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

def node_position(head, X):
    current = head
    count=1
    while current is not None:
        if current.value == X:
            return count
        current = current.next
        count+=1
    return -1
