class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Tree(Node):
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value <= root.val:
                if root.left == None:
                    root.left = Node(value)
                else:
                    root.insert(root.left, value)
            else:
                if root.right == None:
                    root.right = Node(value)
                else:
                    self.insert(root.right, value)

    def printPreorder(self, root):
        if root == None:
            return
        print("{}".format(root.val), end=" ")
        self.printPreorder(root.left)
        self.printPreorder(root.right)

    def printInorder(self, root):
        if root is None:
            return
        self.printPreorder(root.left)
        print("{}".format(root.val), end=" ")
        self.printPreorder(root.right)

    def printPostorder(self, root):
        if root is None:
            return
        self.printPreorder(root.left)
        self.printPreorder(root.right)
        print("{}".format(root.val), end=" ")

if __name__ == "__main__":
    c = Tree()
    c.insert(c.root, 1)
    c.insert(c.root, 2)
    c.insert(c.root, 3)
    c.insert(c.root, 4)
    c.insert(c.root, 5)
    c.insert(c.root, 6)

    c.printPreorder(c.root)
    print()
    c.printInorder(c.root)
    print()
    c.printPostorder(c.root)
    print()
