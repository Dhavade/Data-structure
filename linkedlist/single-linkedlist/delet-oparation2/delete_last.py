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
   
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we cant delete npde !")
        else:
            self.head=self.head.ref

    def delete_last(self):
        if self.head is None:
            print("LL is empty so we cant delete npde !")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None   
            
             

ll1=linkedlist()
ll1.add_beginnning(18)  
ll1.add_beginnning(15)   
ll1.add_beginnning(58) 
#ll1.delete_begin() 
ll1.delete_last()
ll1.delete_last()
ll1.print_ll()                      