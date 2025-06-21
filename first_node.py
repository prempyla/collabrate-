'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def first_node(head):
    if head is None:
        return -1
    return head.data
