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

    
    def search(self,data):
        if self.key == data:
            print("Node Found...!")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node Not Found..!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node Not Found...!")

    def traversal(self): #pre-order, 
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.traversal()
        if self.rchild:
            self.rchild.traversal()

root = BinarySearchTree(100)

list1 = [10,20,30,300,200,150]

for i in list1:
    root.insert(i)
# root.lchild = BinarySearchTree(9)
# print(root.key)
# print(root.lchild)
# print(root.rchild)
# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)

root.search(50)

root.traversal()