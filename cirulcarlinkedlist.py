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
        while n.nref is not self.head:
            print(str(n.data)+" --->",end="")
            n = n.nref
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
    # def insert_middle(self,data):

cl = circularlinkedlist()
cl.insert_begin(10)
cl.insert_end(11)
cl.print()