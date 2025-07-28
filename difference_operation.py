'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
def calculateDifference(root):
    if root is None:
        return 0
    
    current = root
    while current.left is not None:
        current = current.left
    min_val = current.data
    
    current = root
    while current.right is not None:
        current = current.right
    max_val = current.data
    
    product = min_val * max_val
    sum_val = min_val + max_val
    
    return product - sum_val
