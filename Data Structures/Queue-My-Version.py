class queue():
    
    def __init__(self, name=None ,capacity=0):
        self.name=name
        self.queue=[]
        self.size=capacity
        print("queue is initialised and the name of queue is:",self.name)
    def enqueue(self,item):
        if self.size==len(self.queue):
            return print("Queue is Full")
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)==0:
            print("queue is already empty")
        else:
            self.queue.pop(0)
    def display(self):
        return print(self.queue)
    def isFull(self):
        return (self.size==len(self.queue))
    def isEmpty(self):
        return (len(self.queue)==0)

s1=queue("queue1",5)
s2=queue("queue2",2)
print(s1.isEmpty())
print(s2.isEmpty())
s1.enqueue(10)
s1.enqueue("Sachin")
print(s1.isFull())
s1.enqueue("100-Centuries")
s2.enqueue(18)
s2.enqueue("Kohli")
print(s2.isFull())
s2.enqueue("72-Centuries")

s1.dequeue()
s1.display()
s2.display()

# string1=""
# for item in s1.queue:
#     string1+=str(item)+" "
# print(string1)
# string2=""
# for item in s2.queue:
#     string2+=str(item)+" "
# print(string2)

# s2.dequeue()
# string3=""
# for item in s2.queue:
#     string3+=str(item)+" "
# print(string3)

# s2.display()