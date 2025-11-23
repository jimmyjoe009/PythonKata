# Print all the numbers in a binary tree in order
# Traverses the tree using a recursive function

# First let's define the data structures necessary to handle a binary tree
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        curr = self.root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    break

# Create the binary tree
tree=BST()
# Add sample data for testing
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(5)
tree.insert(15)

root=tree.root

# Define the traverse function
def traverse(root):
    if (root.left):
        traverse(root.left)
    print(root.val)
    if (root.right):
        traverse(root.right)

# Run the traversal to print the numbers in order
traverse(root)
