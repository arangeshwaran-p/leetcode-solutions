

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        temp = self.head

        for i in range(index):
            if temp is None:
                return -1
            temp = temp.next

        if temp is None:
            return -1

        return temp.val

    def addAtHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val):
        newnode = Node(val)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newnode

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0

        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        newnode = Node(val)
        newnode.next = temp.next
        temp.next = newnode

    def deleteAtIndex(self, index):
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None or temp.next is None:
            return

        temp.next = temp.next.next

