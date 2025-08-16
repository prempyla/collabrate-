'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def find_min_max(root):
    lst=[]
    inorder(root,lst)
    return lst[0],lst[-1]

def inorder(root,lst):
    if root is None:
        return
    inorder(root.left,lst)
    lst.append(root.val)
    inorder(root.right,lst)
