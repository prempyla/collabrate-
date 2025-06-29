'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

def count_nodes(head):
    count = 1
    if head is None:
        return 0
    while head.next is not None:
        head = head.next
        count+=1
    return count
