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
    '''
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
                n.nref = new_node
        '''

    
    # def insert_before(self,data,x):
        # new_node = Node(data)



dll = DoublyLinkedList()
dll.insert_empty(10)
dll.insert_begin(13)
dll.insert_begin(11)
dll.insert_begin(12)
dll.insert_end(99)
dll.insert_after(99,10)
dll.printlist()
dll.printlistreverse()