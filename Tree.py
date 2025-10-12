from collections import deque

class Node:
    def __init__(self, val=None,
                 left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)
        self.max_var = 0

    def _print_inorder(self, current: Node):
        if not current: return
        self._print_inorder(current.left)
        print(current.val)
        self._print_inorder(current.right)
    
    def print_inorder(self):
        self._print_inorder(self.root)


    def add(self, values_list, direction_list):  
        assert len(values_list) == len(direction_list)
        current = self.root
        for value, direction in zip(values_list, direction_list):
            if direction == 'L':
                if not current.left:
                    current.left = Node(value)
                current = current.left
            elif direction == 'R':
                if not current.right:
                    current.right = Node(value)
                current = current.right
            else:
                raise ValueError("Direction must be 'L' or 'R'")

    def _get_max(self, current:Node):
        if not current: return
        if current.val  > self.max_var: self.max_var = current.val
        self._get_max(current.left)
        self._get_max(current.right)

    def get_max(self):
        self._get_max(self.root)
        return self.max_var


# Example usage: add some leaf nodes to the tree
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.add([ 5, 3, 4, 5, 6, 7], [ 'L','R', 'L','R', 'L','R'])
    # Print inorder traversal
    print(tree.get_max())



