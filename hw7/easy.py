'''Write a Python function to insert a value into a binary search tree. 
The function should take the root of the tree and the value to be inserted 
as parameters. '''

class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# each node stores three things:
# value - number stored in the node
# left - the left child
# right - the right child

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left,  value)

    elif value > root.value:
        root.right = insert(root.right, value) 

    return root

# create tree and insert values

root = Node(13)

root = insert(root, 5)
root = insert(root, 11)
root = insert(root, 9)

print(root.left.right.value) 