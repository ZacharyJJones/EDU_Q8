
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + str(current.data) + "->"
            current = current.next
        return result[:-2]

    def append(self, value):
        # check for empty list
        if self.head is None:
            self.insert_head(value)
            return

        # move to end of list
        current = self.head
        while current.next is not None:
            current = current.next

        # Now at the last node in list
        current.next = Node(value)
        self.size += 1

# ASSIGNMENT ON LINKEDLIST CONTENT HERE
# 1. insertAtIndex(self, pos, value): It will insert a node in anywhere we want in the LinkedList.
# 2. Clear(): It will clear all the nodes.

    def insertAtIndex(self, pos, value):
        if (pos < 0):
            print("IndexError - Position given to insert was negative")
            return
        if (pos > self.size):
            print("IndexError - Position given to insert was outside of LinkedList")
            return
        if (pos == 0):
            self.insert_head(value)
            return

        index = 1
        node_before_insert = self.head
        while (index < pos):
            node_before_insert = node_before_insert.next
            index += 1
            pass

        new_node = Node(value)
        new_node.next = node_before_insert.next
        node_before_insert.next = new_node
        self.size += 1
        pass

    def Clear(self):
        self.head = None
        self.size = 0
        pass

linklist = LinkedList()
linklist.append(100)
linklist.append(200)
linklist.insert_head(300)
linklist.append(400)
linklist.append(500)
linklist.insertAtIndex(2, 1010101)
print(str(linklist))