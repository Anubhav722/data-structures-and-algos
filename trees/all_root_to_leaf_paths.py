class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

blah = []

def printAllPaths(root):
    path = []
    ele = []
    return printPaths(root, path, 0)


def printPaths(root, path, pathLen):
    if not root:
        return

    if len(path) > pathLen:
        path[pathLen] = root.val
    else:
        path.append(root.val)

    pathLen = pathLen + 1

    if root.left is None and root.right is None:
        return path
    else:
        printPaths(root.left, path, pathLen)
        printPaths(root.right, path, pathLen)

def binaryTreePaths(root):
    if root is None:
        return []
    if (root.left == None and root.right == None):
        return [str(root.val)]

    # subtree is always a list, though it might be empty
    left_subtree = binaryTreePaths(root.left)
    right_subtree = binaryTreePaths(root.right)
    full_subtree = left_subtree + right_subtree  # the last part of comprehension

    # full_subtree.insert(0, root.val)
    # full_subtree = [int(i) for i in full_subtree]

    import ipdb; ipdb.set_trace()
    list1 = []

    # list1.append(full_subtree)
    #wide = [root.val]
    for leaf in full_subtree:  # middle part of the comprehension
        #wide.append(left)
        #list1.append(wide)
        list1.append(str(root.val) + '->'+ leaf)  # the left part
        # wide.append(

    return list1
