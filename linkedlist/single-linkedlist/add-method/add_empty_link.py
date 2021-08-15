class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty !")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_beginnning(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def inser_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")


ll1=linkedlist()
ll1.inser_empty(19)
ll1.inser_empty(16)
ll1.print_ll()                
