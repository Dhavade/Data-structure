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
                print(n.data ,end="----->")
                n=n.ref

    def add_beginnning(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LL !")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty !")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node  
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not found !") 
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node       


ll1=linkedlist()
#ll1.add_beginnning(10)
#ll1.add_end(100)
#ll1.add_before(400,100)
ll1.add_after(300,100)
ll1.print_ll()            