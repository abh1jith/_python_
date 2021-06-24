# Queue implementation using Linked Lists



class Node:
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode


class Queue:
    def __init__(self):
        self.head = None

    def peek(self):
        if(self.head == None):
            print(None)
            return
        CurrentNode = self.head
        print(CurrentNode.data)
    
    def enqueue(self, value):
        newnode = Node(value)
        if(self.head == None):
            self.head = newnode
        else:
            CurrentNode = self.head
            while(CurrentNode.nextnode != None):
                CurrentNode = CurrentNode.nextnode
            CurrentNode.nextnode = newnode
            newnode.nextnode = None
            del(CurrentNode)
    
    def dequeue(self):
        if(self.head == None):
            print(None)
            return
        CurrentNode = self.head
        self.head = CurrentNode.nextnode
        del(CurrentNode)

Q = Queue()
"""
Abhijith
Akash
Alankrutha
"""
Q.enqueue("Joy")
Q.enqueue("Matt")
Q.enqueue("Pavel")
Q.enqueue("Samir")
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()


Q.peek()