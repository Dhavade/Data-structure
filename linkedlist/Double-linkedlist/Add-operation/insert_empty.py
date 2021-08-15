class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doubly_LL:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("liked list is empty !")
        else:
            n=self.head
            while n is not None:
                print(n.data,'----->',end=" ")
                n=n.nref 

    def print_LL_reverse(self):
        if self.head is None:
            print("liked list is empty !")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,'----->',end=" ")
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is not empty !")


dl1=doubly_LL()
dl1.insert_empty(18)
dl1.print_LL()                            