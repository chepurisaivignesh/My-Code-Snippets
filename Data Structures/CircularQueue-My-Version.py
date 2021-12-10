class circularqueue:
    def __init__(self,capacity):
        self.cirq=[None]*capacity
        self.cirqcapacity=capacity
        self.head=0
        self.tail=0
        self.size=0

    def isFull(self):
        if self.size==self.cirqcapacity: return True
        return False

    def isEmpty(self):
        if self.size==0: return True
        return False

    def enqueue(self,value):
        if self.isFull(): return None
        self.cirq[self.tail]=value
        self.size+=1
        self.tail=(self.tail+1)%self.cirqcapacity
        return True

    def dequeue(self):
        if self.isEmpty(): return None
        self.size-=1
        self.head=(self.head+1)%self.cirqcapacity
        return True

    def peek(self):
        if self.isEmpty():return -1
        return self.cirq[self.head]

    def rear(self):
        if self.isEmpty():return -1
        return self.cirq[self.tail-1]

c1=circularqueue(5)
print(c1.isEmpty())
print(c1.enqueue(1))
print(c1.enqueue(2))
print(c1.peek())
print(c1.rear())
print(c1.enqueue(3))
print(c1.isEmpty())
print(c1.enqueue(4))
print(c1.peek())
print(c1.rear())
print(c1.enqueue(5))
print(c1.isFull())
print(c1.dequeue())
print(c1.peek())
print(c1.rear())
print(c1.isFull())

