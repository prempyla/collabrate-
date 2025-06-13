'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
'''

def is_palindrome(node):
    lst = []
    current = node
    while current:
        lst.append(current.val)
        current = current.next
    return lst == lst[::-1]
