'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
def findFloor(root, key):
    result = None
    while root:
        if root.val > key:
            root = root.left
        else:
            result = root
            root = root.right
    return result
