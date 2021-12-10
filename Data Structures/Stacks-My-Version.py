class stack():
    
    def __init__(self, name):
        self.name=name
        self.stack=[]
        print("Stack is initialised and the name of stack is:",self.name)
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        if len(self.stack)==0:
            return print("Stack is already empty")
        else:
            return self.stack.pop()
    def display(self):
        return print(self.stack)

    def __repr__(self) -> str:
        self.string=""
        for item in self.stack:
            self.string+=str(item)+" "
        return self.string

s1=stack("STACK1")
s2=stack("STACK2")
s1.push(10)
s1.push("Sachin")
s1.push("100-Centuries")
s2.push(18)
s2.push("Kohli")
s2.push("72-Centuries")

print(s1)#REPR
print(s2)#REPR
s1.display()
s2.display()

print("Peek:",s1.stack[-1])

string1=""
for item in s1.stack:
    string1+=str(item)+" "
print(string1)
string2=""
for item in s2.stack:
    string2+=str(item)+" "
print(string2)

s2.pop()
string3=""
for item in s2.stack:
    string3+=str(item)+" "
print(string3)

s2.display()


# STACK WITHOUT CLASS 

# s1=stack("STACK1")
# s2=stack("STACK2")
# s1.stack.append(10)
# s1.stack.append("Sachin")
# s1.stack.append("100-Centuries")
# s2.stack.append(18)
# s2.stack.append("Kohli")
# s2.stack.append("72-Centuries")
# string1=""
# for item in s1.stack:
#     string1+=str(item)+" "
# print(string1)
# string2=""
# for item in s2.stack:
#     string2+=str(item)+" "
# print(string2)



        