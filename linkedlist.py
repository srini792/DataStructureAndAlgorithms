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

# linkedlistobj = linkedlist()
l1 = linkedlist()
# l1.add_begin(7)
# l1.add_end(10)
# l1.add_begin(4)
# l1.add_end(11)
# l1.add_begin(1)
l1.add_begin(10)
l1.add_end(20)
l1.after_node(15,10)
l1.before_node(12,15)
l1.before_node(9,10)
l1.before_node(9,100)
l1.printll()