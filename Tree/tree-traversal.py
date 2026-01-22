class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
# print Node first and get the value
def preOrder(root):
    if(root != None):
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)
        
        
# print left first and then NODE value after that print right
def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)
        
        
def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")
        
        
        
            
root = Node(1)
root.left= Node(2)
root.right = Node(5)
root.left.left = Node(10)
root.left.right = Node(20)
root.right.left = Node(30)
root.right.right = Node(40)

# preOrder(root)
# inOrder(root)
postOrder(root)