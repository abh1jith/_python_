# Google
# Udemy.com
# Youtube

class Node:
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode

class Stack:
    def __init__(self):
        self.head = None
    
    def Push(self, value):
        NewNode = Node(value)
        if(self.head == None):
            self.head = NewNode
            NewNode.nextnode = None
        else:
            CurrentNode = self.head
            while(CurrentNode.nextnode != None):
                CurrentNode = CurrentNode.nextnode
            CurrentNode.nextnode = NewNode
            NewNode.nextnode = None
    
    def pop(self):
        if(self.head == None):
            print("Empty Stack")
            return
        else:
            CurrentNode = self.head
            while(CurrentNode.nextnode != None):
                PrevNode = CurrentNode
                CurrentNode = CurrentNode.nextnode
            PrevNode.nextnode = None
            del(CurrentNode)
    
    def peek(self):
        if(self.head == None):
            print("Empty Stack")
            return
        else:
            CurrentNode = self.head
            while(CurrentNode.nextnode != None):
                CurrentNode = CurrentNode.nextnode
            print(CurrentNode.data)

Stack = Stack()
Stack.Push("Youtube")
Stack.peek()
Stack.Push("Google")
Stack.peek()
Stack.Push("Udemy")
Stack.peek()
Stack.pop()
Stack.peek()