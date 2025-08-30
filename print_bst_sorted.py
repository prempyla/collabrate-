'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def sorted_order(root):
    lst=[]
    inorder(root,lst)
    return lst

def inorder(root,lst):
    if root is None:
        return 
    inorder(root.left,lst)
    lst.append(root.val)
    inorder(root.right,lst)

# inorder will give us in sorted_order
