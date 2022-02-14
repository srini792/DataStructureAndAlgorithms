class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None


class linkedlist():
    def __init__(self):
        self.head = None


    def printll(self):
        if self.head is None:
            print("linked list is empty....")
        else:
            n = self.head
            while n is not None:
                print(str(n.data)+"--->",end=" ")
                n = n.ref

    def insertemptylist(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("list is not empty to insert ON insertemptylist")
        
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node 

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        
    def after_node(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("The element is not present to insert inbetween")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self,data,x):
        n = self.head
        if n is None:
            print("Action can't be done because linked list is empty")
            return
        if n.data==x:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Action can't be done because linked list does not have searching element")
            return           
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_first(self):
        if self.head is None:
            print("linked list is empty so we can't perform any deletion...")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
             print("linked list is empty so we can't perform any deletion...")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            # print(n.data)
            n.ref = None
    def delete_value(self,data):
        if self.head is None:
            print("linked list is empty so we can't delete any element")
            return
        if data==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==data:
                break
            n = n.ref
        if n.ref is None:
            print("element to get delete is not present in linked list")
            return
        else:
            n.ref = n.ref.ref
            



# linkedlistobj = linkedlist()
l1 = linkedlist()

l1.add_begin(7)
l1.insertemptylist(1)
l1.add_end(10)
l1.add_begin(4)
l1.add_end(11)
l1.add_begin(8)
l1.delete_value(7)
# l1.add_end(18)
# l1.delete_first()
# l1.delete_end()
# l1.add_begin(1)
# l1.add_begin(10)
# l1.add_end(20)
# l1.after_node(15,10)
# l1.before_node(12,15)
# l1.before_node(9,10)
# l1.before_node(9,100)
l1.printll()