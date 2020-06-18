"""
Author: Atharva Muley
Date: Jan 30 2020
"""
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1

class Tree(Node):
    def __init__(self, avl_tree = False):
        self.root = None
        self.avl = avl_tree

    def insert(self, root, value):
        
        if self.root == None:
            self.root = Node(value)
            return
        else:
            if value < root.val:
                if root.left == None:
                    root.left = Node(value)
                else:
                    root.insert(root.left, value)
            elif value > root.val:
                if root.right == None:
                    root.right = Node(value)
                else:
                    self.insert(root.right, value)
        # print("ROot", root)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalanceFactor(root)
        # print(balance)

        #Right Right
        if balance < -1 and value > root.right.val:
            return self.leftRotate(root)
        
        #Right Left
        if balance < -1 and value < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        #Left Left
        if balance > 1 and value < root.left.val:
            return self.rightRotate(root)
        
        #Left Right
        if balance > 1 and value > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

    def leftRotate(self, root):
        y = root.right
        z = y.left

        #rotation
        y.left = root
        root.right = z

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, root):
        y = root.left
        z = y.right

        #rotation
        y.right = root
        root.left = z

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def printPreorder(self, root):
        if root is None:
            return
        print("{}".format(root.val), end=" ")
        self.printPreorder(root.left)
        self.printPreorder(root.right)

    def printInorder(self, root):
        if root is None:
            return
        self.printInorder(root.left)
        print("{}".format(root.val), end=" ")
        self.printInorder(root.right)

    def printPostorder(self, root):
        if root is None:
            return
        self.printPostorder(root.left)
        self.printPostorder(root.right)
        print("{}".format(root.val), end=" ")

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
        
if __name__ == "__main__":
    c = Tree(avl_tree = True)
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
    print("H", c.getHeight(c.root))