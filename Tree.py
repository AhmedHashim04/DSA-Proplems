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


    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.val))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

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

    ###############################

    
    def tree_max(self):
        print("tree_max called")
        return self._tree_max(self.root)
        
    def _tree_max(self, current):
        print(f"_tree_max called with node: {current.val if current else None}")
        if not current:
            return float("-inf")

        result = max(current.val, self._tree_max(current.left), self._tree_max(current.right))
        print(f"Returning max({current.val}, {self._tree_max(current.left)}, {self._tree_max(current.right)}) = {result}")
    
        return result
    ######################
    def _maxDepth(self, current):
        if not current: return 0
        return 1 + max(self._maxDepth(current.left), self._maxDepth(current.right))


    
    def maxDepth(self):
        return self._maxDepth(self.root)
    ##################
    def _sum_of_left_leaves(self, current, is_left = False):
        if not current : return 0
        if not(current.left and current.right):    
            if is_left :
                return current.val
            else :
                return 0

        left_sum = self._sum_of_left_leaves(current.left,True)
        right_sum = self._sum_of_left_leaves(current.right)

        return left_sum + right_sum

    def sum_of_left_leaves(self):
        return self._sum_of_left_leaves(self.root)

    ##################
    # Cusins must have same level and must not have same parent
    def _Cusins(self, current, lev1 = -8, lev2= -8, parent1= -8, parent2= -8):
        if not current : return 0
        first_child  = self._Cusins(current.left, lev1+1,parent1=current) 
        secon_child  = self._Cusins(current.right, lev2+1,parent2=current)

        print(parent1 == parent2, lev1 == lev2)
    def Cusins(self):
        return self._Cusins(self.root)




# Example usage: add some leaf nodes to the tree
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.add([ 5, 3, 4, 8, 6, 7], [ 'L','R', 'L','R', 'L','R'])
    # print(tree.print_tree(tree.root))
    # print(tree.sum_of_left_leaves())
    print(tree.tree_max())

