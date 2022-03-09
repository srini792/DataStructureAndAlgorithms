class BinarySearchTree():
    def __init__(self,key): # every node in tree is object of this class
        self.key = key
        self.lchild = None
        self.rchild = None

root = BinarySearchTree(10)
root.lchild = BinarySearchTree(9)
print(root.key)
print(root.lchild)
print(root.rchild)
print(root.lchild.key)
print(root.lchild.lchild)
print(root.lchild.rchild)