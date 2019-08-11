class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def search(root, key):
    while root and root.val != key:
        if root.val > key:
            root = root.left
        else:
            root = root.right
    return root


def insert(root, node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None:
                root.right = node 
            else: 
                insert(root.right, node)
        else: 
            if root.left is None:
                root.left = node
            else: 
                insert(root.left, node)


r = TreeNode(50) 
insert(r, TreeNode(30)) 
insert(r, TreeNode(20)) 
insert(r, TreeNode(40)) 
insert(r, TreeNode(70)) 
insert(r, TreeNode(60)) 
insert(r, TreeNode(80)) 
node = search(r, 30)
print (node.left.val)
print (node.right.val)