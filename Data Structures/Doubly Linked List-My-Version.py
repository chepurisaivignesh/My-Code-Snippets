class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DoublyLL:
    def __init__(self):
        self.head=None
    
    def showForwardDLL(self):
        value=""
        k=self.head
        if k==None:
            print("Doubly Linked list is empty.")
        else:
            while k is not None:
                value+=(str(k.data)+"-->")
                k=k.nref
            return value

    def showBackwardDLL(self):
        value=""
        o=self.head
        if o==None:
            print("Doubly Linked list is empty.")
        else:
            while o.nref is not None:
                o=o.nref            
            while o is not None:
                value+=(str(o.data)+"-->")
                o=o.pref
            return value

    def addfirst(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("Linked List is not empty.")

    def addbegin(self,data):
        if self.head is None:
            self.addfirst(data)
        else:
            newnode=Node(data)
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode

    def addend(self,data):
        if self.head is None:
            self.addfirst(data)
        else:
            j=self.head
            while j.nref is not None:
                j=j.nref 
            newnode=Node(data)
            j.nref=newnode
            newnode.pref=j

    def afternode(self,data,afnode):
        if self.head is None:
            print("Linked List is empty.")
        else:
            u=self.head
            while u.data is not afnode:
                u=u.nref
            if u is None:
                print("Linked List does not have the value you asked for.")
            else:
                newnode=Node(data)
                newnode.nref=u.nref
                newnode.pref=u
                if u.nref is not None:
                    u.nref.pref=newnode
                u.nref=newnode
    
    def beforethenode(self,data,beforenode):
        if self.head is None:
            print("Linked List is empty.")
        else:
            v=self.head
            while v.data is not beforenode:
                v=v.nref
            if v is None:
                print("Linked List does not have the value you asked for.")
            else:
                newnode=Node(data)
                newnode.pref=v.pref
                newnode.nref=v
                if v.pref is not None:
                    v.pref.nref=newnode
                else:
                    self.head=newnode
                v.pref=newnode
    
    def delbegin(self):
        if self.head is None:
            print("Linked List is empty.")
        elif self.head.nref is None:
            self.head=None
            print("Linked List is empty after deleting the node.")
        else:
            self.head=self.head.nref
            self.head.pref=None
    
    def delend(self):
        if self.head is None:
            print("Linked List is empty.")
        elif self.head.nref is None:
            self.head=None
            print("Linked List is empty after deleting the node.")
        else:
            b=self.head
            while b.nref is not None:
                b=b.nref
            b.pref.nref=None
    
    def delbyvalue(self,value):
        if self.head is None:
            print("Linked List is empty.")
        elif self.head.nref==None:
            if self.head.data==value:
                self.head=None
                print("Linked List is empty after deleting the node.")
                return
            else:
                print("Linked List do not have your value.")
                return
        elif self.head.data==value:
            self.head=self.head.nref
            self.head.pref=None
            return
        i=self.head
        while i.nref is not None:
            if i.data==value:
                break
            i=i.nref
        if (i.nref is not None):
            i.nref.pref=i.pref
            i.pref.nref=i.nref
            return
        else:
            if(i.data==None):
                i.pref.nref=None
                return
            else:
                print("Linked List do not have your value.")
                return









