# Binary search tree>>


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
        
def insert(root, value):
        if (root == None):
            return Node(value)
        
        if(root.data == value):
            return root
        
        if(root.data > value):
            root.left = insert(root.left, value)
            
        else:
            root.right = insert(root.right, value)  
        return root # agar koi sa block nhi chlta to ye chalega>>
    
    
def search(root, value):
    if(root == None):
        print("Element not found")
        return
        
    if(root.data == value):
        print("Element found: ", value)
        return
        
    if(root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)
        
def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root        
        
def deletion(root, value):
    if(root == None):
        return root
    if (root.data > value):
        root.left = deletion(root.left, value)
    elif (root.data < value):
        root.right = deletion(root.right, value)
    
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = deletion(root.right, succ.data)
            
    return root
            

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)
        
        


root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)


# inOrder(root)
# search(root, 18) # 18 exist
# search(root, 100) # 100 not exist 

# deletion(root,12) # delete who have singel child
print("\n")
inOrder(root)

deletion(root, 30)
inOrder(root)
