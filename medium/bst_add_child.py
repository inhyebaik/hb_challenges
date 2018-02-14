class Node(object):  # ...
    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data


    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        curr = self
        # first check if it's smaller or larger than current node
        while curr.left or curr.right: # break when we reach leaf
            if new_data > curr.data:

                # check if it has right child:
                if curr.right:
                    curr = curr.right
            
            else: 
                if curr.left:
                    curr = curr.left

        # do final comparison at leaf to add new child
        if new_data > curr.data:
            curr.right = Node(new_data)
        else:
            curr.left = Node(new_data)




t = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(8)))
# Our insert method should do this correctly:
t.insert(0) 
print t.left.left.left.data == 0 # True
print t.left.left.right is None # True

t.insert(9)
print t.right.right.right.data == 9 # True
print t.right.right.left is None # True

t.insert(6)
print t.right.left.right.data == 6 # True
print t.right.left.left is None # True