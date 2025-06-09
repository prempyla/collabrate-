'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def isPositive(head):
    count=0
    current = head
    while current is not None:
        if current.data < 0:
            count+=1
        current = current.next
    if count%2==0:
        return "Yes"
    else:
        return "No"
