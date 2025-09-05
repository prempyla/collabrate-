'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
def left_subtree_max(root):
    if root is None:
        return -1
    if root.left is None:
        return -1
    return maxi(root.left)
    
def maxi(root):
    if root.right is None:
        return root.val
    return maxi(root.right)
