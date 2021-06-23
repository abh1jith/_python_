# Class for Node. Has data and link attributes
class Node:
	def __init__(self, data, NextNode = None):
		self.data = data
		self.NextNode = NextNode
# Class for Linked List
class LinknedList:
	# Initially the Linked List has only a head Node. The head node does not have a data value
	def __init__(self):
		self.head = None
# Print the Linked List
	def PrintList(self):
		if(self.head != None):
			CurrentNode = self.head
			while(CurrentNode.NextNode != None):
				print(CurrentNode.data, end = " -> ")
				CurrentNode = CurrentNode.NextNode
			print(CurrentNode.data, end = " -> ")
		print(None)
# Insert a node at the End
	def InsertAtEnd(self, value):
		# Create a new node for the given value
		NewNode = Node(value)
		if(self.head == None):
			self.head = NewNode
			NewNode.NextNode = None
		else:
			CurrentNode = self.head
			while(CurrentNode.NextNode != None):
				CurrentNode = CurrentNode.NextNode
			CurrentNode.NextNode = NewNode
			NewNode.NextNode = None
# Insert a node at the beginning
	def InsertAtBeg(self, value):
		# Create a new node for the given value
		NewNode = Node(value)
		temp = self.head
		self.head = NewNode
		NewNode.NextNode = temp
		del(temp)
# Insert a node at a specific Index
	def InsertAt(self, index, value):
		# Create a new node for the given value
		NewNode = Node(value)
		pos = 1
		CurrentNode = self.head
		while(pos < index):
			CurrentNode = CurrentNode.NextNode
			pos = pos + 1
		temp = CurrentNode.NextNode
		CurrentNode.NextNode = NewNode
		NewNode.NextNode = temp
		del(temp)
# Deleting a node at the beginning
	def DeleteAtBeg(self):
		if(self.head == None):
			return
		else:
			temp = self.head.NextNode
			self.head = temp
			del(temp)
# Deleting a node at the end
	def DeleteAtEnd(self):
		if(self.head == None):
			return
		else:
			temp = self.head
			while(temp.NextNode != None):
				# Previous Node to keep track of it and change it to None
				PrevNode = temp
				temp = temp.NextNode
			PrevNode.NextNode = None
			del(temp)
# Deleting a node at a spcific Index
	def DeleteAt(self, index):
		CurrentNode = self.head
		PrevNode = CurrentNode
		p = 1
		while(p < index):
			PrevNode = CurrentNode
			CurrentNode = CurrentNode.NextNode
			p = p + 1
		PrevNode.NextNode = CurrentNode.NextNode
		del(CurrentNode)
		del(p)





li = LinknedList()
li.InsertAtEnd(1)
li.InsertAtEnd(3)
li.InsertAtBeg(0)
li.InsertAt(2, 2)
li.DeleteAt(2)
li.PrintList()
