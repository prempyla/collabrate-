'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
def isBST(root):
    def solver(node, min_, max_):
        if node is None:
            return True
        left = solver(node.left, min_, node.val)
        right = solver(node.right, node.val, max_)
        return min_ < node.val < max_ and left and right
    
    return solver(root, float('-inf'), float('inf'))
