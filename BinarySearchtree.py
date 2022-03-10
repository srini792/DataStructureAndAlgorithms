class BinarySearchTree():
    def __init__(self,key): # every node in tree is object of this class
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BinarySearchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BinarySearchTree(data)

root = BinarySearchTree(10)
root.lchild = BinarySearchTree(9)
print(root.key)
print(root.lchild)
print(root.rchild)
print(root.lchild.key)
print(root.lchild.lchild)
print(root.lchild.rchild)