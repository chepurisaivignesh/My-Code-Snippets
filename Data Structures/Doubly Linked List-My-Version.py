class Node:
    def __init__(self,data):
        self.data=data
        nref=None
        pref=None

class DoublyLL:
    def __init__(self):
        self.head=None
    
    def showForwardDLL(self):
        k=self.head
        if k==None:
            print("Doubly Linked list is empty.")
        else:
            while k is not None:
                print(k.data,end="-->")
                k=k.nref
            print(k)
    
    def showBackwardDLL(self):
        o=self.head
        if o==None:
            print("Doubly Linked list is empty.")
        else:
            while o.nref is not None:
                o=o.nref
            print(o)
            while o is not None:
                print(o.data,end="-->")
                o=o.pref

dl1=DoublyLL()
dl1.showForwardDLL()
dl1.showBackwardDLL()
