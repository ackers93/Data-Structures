from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # setting conditionals
        if type(value) is not int:
            raise ValueError("Not an int")
        if self.value == None:
            self.value = value
            return
        elif value < self.value:  # the value passed in by the insert
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if type(target) is not int:
            raise ValueError("Not an int")
        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.right.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        print(self.value)
        cb(self.value)
        if self.left:
            print('left')
            self.left.for_each(cb)
        if self.right:
            print('right')
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
