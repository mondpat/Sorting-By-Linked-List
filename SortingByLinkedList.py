import sys

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
            while(temp.next != None and new.val > temp.next.val):
                temp = temp.next
            new.next = temp.next
            temp.next = new

    def delete(self):
        if(self.begin == None):
            return None
        if(self.begin.next == None):
            delete = self.begin
            self.begin = None
            return delete
        delete = self.begin.next.val
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