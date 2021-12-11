class Node:
    def __init__(self,data=None):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
        # print("New Linked List is Created")

    def showLL(self):
        print(self.__class__.__name__)
        if self.head==None:
            print("The Linked List is empty.")
        else:
            n=self.head
            stringy=""
            while n is not None:
                if n.ref==None:
                    stringy=stringy+str(f"[{n.data},{n.ref}]")
                else:
                    stringy=stringy+str(f"[{n.data},{n.ref}]")+"-->"
                n=n.ref
            # print("Linked List:")
            print(stringy)

    def add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
        # print("New node is added at the start and it is the new head.")
        # print(self.head)
        # print(newnode.ref)

    def add_end(self,data):
        newnode=Node(data)
        if self.head==None:
            newnode.ref=self.head
            self.head=newnode
            # print("New node is added at the start and it is the new head.")
        else:
            k=self.head
            while k.ref is not None:
                k=k.ref
                # print(k)
            k.ref=newnode
            # print("New node is added at the end .")
            
    def add_after_node(self,data,afterthenode):  
        m=self.head
        while m is not None:
            if afterthenode==m.data:
                break
            m=m.ref
        if m is None:
            print("Item is not present in the Linked-List")
        else:
            newnode=Node(data)
            newnode.ref=m.ref
            m.ref=newnode
            # print(f"New node is added in between {m.data} and {newnode.ref.data}")
    
    def add_before_node(self,data,beforethenode):
        if self.head==None:
            print("Linked List is Empty")
            return
        if self.head.data==beforethenode:
            newnode=Node(data)
            newnode.ref=self.head
            self.head=newnode
            return
        o=self.head
        while o.ref is not None:
            if o.ref.data==beforethenode:
                break
            o=o.ref
        if o.ref==None:
            print("Node is not found")
        else:
            newnode=Node(data)
            newnode.ref=o.ref
            o.ref=newnode

    def del_begin(self):
        if self.head==None:
            print("Linked List is empty, so we cant we delete a node.")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head==None:
            print("Linked List is empty, so we cant we delete a node.")
        elif self.head.ref is None:
            self.head=None
        else:
            i=self.head
            while i.ref.ref is not None:
                i=i.ref
            i.ref=None

    def del_by_value(self,data):
        if self.head==None:
            print("Linked List is empty, so we cant we delete a node.")
        elif self.head.data==data:
            self.head=self.head.ref
        else:
            u=self.head
            while u.ref is not None:
                if u.ref.data==data:
                    break
                u=u.ref
            if u.ref is None:
                print("There is no node of the given value.")
            else:
                u.ref=u.ref.ref
L=Linkedlist()
L.add_begin(20)
L.add_begin(10)
L.showLL()
L.add_end(30)
L.showLL()
L.add_begin(40)
L.showLL()
L.add_after_node(40,20)
L.showLL()
L.add_after_node(50,40)
L.showLL()
