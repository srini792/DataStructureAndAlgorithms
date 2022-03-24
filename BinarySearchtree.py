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

    def traversalInorder(self):
        if self.lchild:
            self.lchild.traversalInorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.traversalInorder()

    def traversalPostOrder(self):
        if self.lchild:
            self.lchild.traversalInorder()
        if self.rchild:
            self.rchild.traversalInorder()
        print(self.key,end=" ")
    
    def DeleteNode(self,data,curr):
        if self.key is None:
            print("Tree is empty..!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.DeleteNode(data,curr)
            else:
                print("data is not present in a tree..!")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.DeleteNode(data,curr)
            else:
                print("data is not present in a tree...!")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.DeleteNode(node.key,curr)
        return self
    def minKey(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(f"the min key is -->{current.key}")
    def maxKey(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(f"the max key is -->{current.key}")

def countNode(node):
    if node is None:
        return 0 
    else:
        return 1+countNode(node.lchild)+countNode(node.rchild)


root = BinarySearchTree(100)

list1 = [50,1,102,1000,0]

for i in list1:
    root.insert(i)


# root.traversal()
# print()
# root.traversalInorder()
# print()

# if countNode(root) > 1:
#     root.DeleteNode(100,root.key)
# else:
#     print(f"Deletion can't perform in this tree..!!")
# root.traversalInorder()

root.minKey()
root.maxKey()