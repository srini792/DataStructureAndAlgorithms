class Node():
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    
    def printlist(self):
        if self.head is None:
            print("Doubly linked list is empty...!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"---> ",end=" ")
                n = n.nref
            print()
    
    def printlistreverse(self):
        if self.head is None:
            print("Doubly linked list is empty...!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"---> ",end=" ")
                n = n.pref
            print()

    def insert_empty(self,data):
        if self.head is not None:
            print("doubly linked list is not empty to insert....!")
        else:
            new_node = Node(data)
            self.head = new_node
    
    def insert_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    def insert_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print("The list is empty so we could not add any given element....!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print("element is not present in linked list...!")
                return
            elif n.nref is None:
                new_node.pref = n
                n.nref = new_node 
            else:
                new_node.pref = n
                new_node.nref = n.nref
                n.nref.pref = new_node
                n.nref = new_node
        
    def insert_before(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print("The list is empty so we could not add any given element....!")
        else:
            n = self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("element is not present in linked list...!")
            elif n.pref is None:
                n.pref = new_node
                new_node.nref = n
                self.head = new_node
            else:
                new_node.nref = n
                new_node.pref = n.pref
                n.pref.nref = new_node
                n.pref = new_node
    # def insert_before(self,data,x):
        # new_node = Node(data)
    def Delete_begin(self):
        if self.head is None:
            print(f"doubly linked list is empty..! so deletion is not")
            return
        if self.head.nref is None:
            self.head = None
            print(f"doubly linked list is empty after deletion...!")
        else:
            self.head = self.head.nref
            self.head.pref = None


    def Delete_end(self):
        if self.head is None:
            print(f"doubly linked list is empty..! so deletion is not")
            return
        if self.head.nref is None:
            self.head = None
            print(f"doubly linked list is empty after deletion...!")
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
        
    def Delete_by_value(self,x):
        if self.head is None:
            print(f"doubly linked list is empty..! so deletion is not")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print(f"element need to be delete is not present in linked list..!")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            else:
                n = n.nref
        if n.nref is not None:
           n.pref.nref = n.nref
           n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(f"element need to be delete is not present in linked list..!") 
        
dll = DoublyLinkedList()
dll.insert_empty(10)
dll.insert_before(11,10)
dll.insert_after(12,11)
dll.insert_begin(100)
dll.Delete_by_value(10)
# dll.insert_begin(11)
# dll.insert_end(13)
# dll.insert_after(12,10)
# dll.insert_before(17,13)
# dll.insert_after(15,14)
# dll.Delete_begin()
# dll.Delete_end()
# dll.insert_begin(11)
# dll.insert_after(12,11)
# dll.insert_end(99)
# dll.insert_after(99,10)
# dll.insert_after(100,99)
# dll.insert_before(101,100)
# dll.Delete_begin()
dll.printlist()
dll.printlistreverse()