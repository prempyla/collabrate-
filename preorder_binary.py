'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def preorder_traversal(root):
    lst=[]
    preorder(root, lst)
    return lst

def preorder(root,lst):
    if root == None:
        return 
    lst.append(root.val)
    preorder(root.left,lst)
    preorder(root.right,lst)
