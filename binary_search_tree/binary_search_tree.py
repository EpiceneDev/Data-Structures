import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return
        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # if smaller, go left
            # if value < node.value look left
                # if something is there already
                # recurse left
            # if not
                # insert left
        # if bigger look right
        # if something is there
            # recureseleft
        # if no node, make one at that spot
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()


# TRAVERSAL
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left FIRST
        if self.left is not None:
            self.left.for_each(cb)
        # print the value
        cb(self.value)
        # go right
        if self.right is not None:
            self.right.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left FIRST
        if node.left is not None:
            node.in_order_print(node.left)

        # Print ourselves
        print(node.value)

        # go right 
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue for nodes
        node_queue = Queue()
        #add current node to queue
        node_queue.insert(node)
        #while the queue is empty
        if node_queue:
            #dequeue node
            Queue.dequeue(node)
            #print node
            print(node)
            # add node children
            if self.left:
                #if left, add 
                Queue.enqueue(self.left, node)
            if self.right:
                #if right, add
                Queue.enqueue(self.right, node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node_stack
        node_stack = Stack()
        # push the current node onto stack
        Stack.push(node_stack, node)
        # while we have items on stack
        if node_stack:
            # print the current value and pop it off
            print(node_stack.value)
            Stack.pop(node_stack)
            # push the right value of the current node if we can
            if node_stack.right:
                Stack.push(node_stack, node)
            # push the left value of current node if we can
            if node_stack.left:
                Stack.push(node_stack, node)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
