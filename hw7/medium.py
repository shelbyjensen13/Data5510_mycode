'''2. Implement a Python function to search for a value in a binary 
search tree. The method should take the root of the tree and the value 
to be searched as parameters. It should return True if the value is found 
in the tree, and False otherwise.'''

class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left,  value)

    elif value > root.value:
        root.right = insert(root.right, value) 

    return root

def search(root, value):
    if root is None:
        return False

    if root.value == value:
        return True

    elif value < root.value:
        return search(root.left, value)

    else:
        return search(root.right, value) 
    


root = Node(8)

root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 6)

print(search(root, 6))
print(search(root, 5))
print(search(root, 10))

