from logging.config import valid_ident
import sys
import tempfile
from tkinter.messagebox import NO

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.begin = None

    def insert(self, NewVal):
        new = Node(NewVal)
        temp = self.begin
        if(temp == None or new.val <= temp.val):
            new.next = self.begin
            self.begin = new
        else:
            InsertNewNodeWhenHeadIsNotEmpty(temp, new)

    def delete(self):
        if(self.begin == None):
            return None
        if(self.begin.next == None):
            delete = self.begin.val
            self.begin = None
            return delete
        delete = self.begin.val
        self.begin = self.begin.next
        return delete

    def DisplayAndDelete(self):
        if(self.begin == None):
            return 0
        temp = self.begin
        while(temp != None):
            print(temp.val, end=" ")
            stack.delete()
            temp = temp.next
    
def InsertNewNodeWhenHeadIsNotEmpty(tempNode: Node, newNode: Node):
        if tempNode.next != None and tempNode.next.val < newNode.val:
            InsertNewNodeWhenHeadIsNotEmpty(tempNode.next, newNode)
        else:
            newNode.next = tempNode.next
            tempNode.next = newNode

def InsertNumbersFromInputToLinekdList():
    char = sys.stdin.read(1)
    num = ""
    while(char != "\n"):
        while(char == ' '):
            char = sys.stdin.read(1)        
        while(ord(char) != 32 and char != "\n"):
            num += char
            char = sys.stdin.read(1)
        if (num != ""):
            stack.insert(int(num))
        num = ""
        if(char != "\n"):
            char = sys.stdin.read(1)

stack = LinkedList()
InsertNumbersFromInputToLinekdList()
stack.DisplayAndDelete()