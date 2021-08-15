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

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node    

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            new_node.pref=n
            n.nref=new_node

    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("Given node is not present is DLL")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("LL is emoty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref  
            if n is None:
                print("Given node is not present in DLL")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node          
                else:
                    self.head=new_node
                n.pref=new_node



    def delete_begin(self):
        if self.head is None:
            print("DLL is empty")
            return
        if self.head.nref is None:
            self.head=None
            print("DLL is empty after deleting tha node !")
        else:
            self.head=self.head.nref
            self.head.pref=None


    def delete_end(self):
        if self.head is None:
            print("DLL is empty !")
            return
        if self.head.nref is None:
            self.head=None
            print("DLL is empty after deleting tha node !")    
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None    


                
dl1=doubly_LL()
dl1.insert_empty(18)
dl1.add_begin(10)
dl1.add_end(49)
dl1.add_after(3,49)
#dl1.add_after(3,3)
dl1.add_before(88,10)
dl1.delete_begin()
dl1.delete_end()

dl1.print_LL()
#dl1.print_LL_reverse()