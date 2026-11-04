'''3. Explain the process of deleting a node from a binary 
search tree in Python. Discuss how you would handle different cases, 
such as deleting a node with one, or two children. Additionally, explain 
any potential challenges or edge cases that may arise during the deletion 
process and how you would address them. '''

# Deleting a node is different depending on how many children it has. To start off, 
# we search for the node we want to remove. After that there are three cases. If 
# it doesn't have any children we can simply remove it by setting the parent pointer
# to "None". If it has one child, we'd replave the node with its child so that the 
# rest of the tree stays connected. If it has two children, we'd find the smallest 
# value in its right subtree, called the inorder successor. Replace the deleted node's 
# value with the successor's value then delete the successor from its original position.

# some challenges may occur during deletion including deleting the root node, 
# deleting a value that doesn't exist, and making sure the tree still follows the binary
# search tree rules after the node is removed. We'd handle them by returning the updated
# root of the tree, leaving the tree unchanged if the value is not found, and carefully
# reconnecting the remaining nodes after deletion. 