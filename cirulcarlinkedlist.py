class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None


class circularlinkedlist():
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print(f"circular linked list is empty...!")
            return
        n = self.head
        if n.nref is self.head:
            print(str(n.data)+" --->",end="")
            return
        else:
            while n.nref is not self.head:
                print(str(n.data)+" --->",end="")
                n = n.nref
            print(str(n.data)+" --->",end="")
            print()


    def insert_begin(self,data):
        new_node = Node(data)
        self.head = new_node
        self.head.nref = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.nref = new_node
            return
        n = self.head
        while n.nref is not n:
            n = n.nref
        new_node.nref = n.nref
        n.nref = new_node
    
    def insert_middle(self,data,x):
        new_node = Node(data)
        n = self.head
        while n.nref is not self.head:
            if n.data == x:
                break
            n = n.nref
        if n.data == x:
            new_node.nref = n.nref
            n.nref = new_node
        else:
            print("unable to insert, element not present in list...!")

    def delete_begin(self):
        if self.head is None:
            print(f"There is no element in list, so deletion operation is not possible..!")
            return
        if self.head.nref is self.head:
            self.head = None
            return
        else:
            n = self.head
            while n.nref is not self.head: 
                n = n.nref
            n.nref = self.head.nref
            self.head = self.head.nref
            return
    
    def delete_end(self):
        if self.head is None:
            print(f"There is no element in list, so deletion operation is not possible..!")
            return
        if self.head.nref is self.head:
            self.head = None
            return
        else:
            n = self.head
            while n.nref.nref is not self.head: 
                n = n.nref
            n.nref = self.head
            return
cl = circularlinkedlist()
cl.insert_begin(10)
cl.insert_end(11)
cl.insert_middle(10.5,11)
cl.insert_middle(12,11)
cl.delete_begin()
cl.delete_end()
cl.print()