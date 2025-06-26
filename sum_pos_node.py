'''
class Node:
    def __init__(self, val=1):
        self.val = val
        self.left = None
        self.right = None
'''

def pos_node_sum(root):
    if root is None:
        return 0

    left_sum = pos_node_sum(root.left)
    right_sum = pos_node_sum(root.right)

    current_val = root.val if root.val > 0 else 0

    return current_val + left_sum + right_sum
