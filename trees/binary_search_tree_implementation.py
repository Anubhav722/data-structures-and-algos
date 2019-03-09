class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)

        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print (root.data),
    in_order_print(root.right)


def pre_order_print(root):
    if not root:
        return

    print (root.data),
    pre_order_print(root.left)
    pre_order_print(root.right)


def post_order_print(root):
    if not root:
        return

    post_order_print(root.left)
    post_order_print(root.right)
    print (root.data),
