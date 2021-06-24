# Binary Search Tree Implementation using OOPS
# This code only does insertion into the tree and looking up wheather the element is present or not.

# Node class for each and every element
class Node:
    def __init__(self, value, left = None, right = None):
        # Data attribute
        self.value = value
        # Left Child attribute
        self.left = left
        # Right child attribute
        self.right = right

# Class for the whole tree
class BinarySearchTree:
    def __init__(self):
        # Initially the tree is empty, so the root node points to NONE
        self.root = None
    
    # Inserting a node into the tree
    def InsertNode(self, value):
        # Creating a node class for the value entered
        NewNode = Node(value)
        # Checking if the tree is empty. If so we can directly update the root node to the entered value
        if(self.root == None):
            self.root = NewNode
        else:
            # If the tree is not empty, we need to traverse through the tree and look up a suitable position for the node to be placed
            CurrentNode = self.root
            # Exit condition is a must!!
            while(True):
                # If the value entered is less than the current node(Initially it is the root node and will update as the loop iterates), we go to the left side of the tree
                if(value < CurrentNode.value):
                    # Left side of tree
                    # If the left side is empty(or None), we add the entered value there
                    if(CurrentNode.left == None):
                        CurrentNode.left = NewNode
                        return
                    # Else, we update the current node to the left side node
                    else:
                        CurrentNode = CurrentNode.left
                # If the value entered is greater than the current node(Initially it is the root node and will update as the loop iterates), we go to the right side of the tree
                else:
                    # Right side of the tree
                    # If the right side is empty(or None), we add the entered value there
                    if(CurrentNode.right == None):
                        CurrentNode.right = NewNode
                        return
                    # Else, we update the current node to the right side node
                    else:
                        CurrentNode = CurrentNode.right

# Checking if the entered value is present in the tree or not
    def lookup(self, number):
        # We start iterating from the root node and move according the conditional statements
        CurrentNode = self.root
        # Exit condition is a must!!!
        while(True):
            # If the number is present we leave the loop
            if(CurrentNode.value == number):
                print(True)
                return
            # This is the important exit condition
            # If there is no left or right subchild for the current node, there will be no place for the loop to iterate. So we leave the loop and the function, since the entered value is npot present.
            if(CurrentNode.left == CurrentNode.right == None):
                print(False)
                return
            # If the number is not found, we check if the number is greater or less than the current node value
            else:
                # If it is greater than the current node, we update the current node to move right for its next iteration
                if(number > CurrentNode.value):
                    CurrentNode = CurrentNode.right
                # If it is less than the current node, we update the current node to move left for its next iteration
                else:
                    CurrentNode = CurrentNode.left
            




BST = BinarySearchTree()
BST.InsertNode(9)
BST.InsertNode(4)
BST.InsertNode(6)
BST.InsertNode(20)
BST.InsertNode(170)
BST.InsertNode(15)
BST.InsertNode(1)
BST.lookup(0)
