class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        """
            function to display the linked list on standard output
        """
        current = self.head
        if self.head:
            while current.next:
                print(str(current.value) + " --> ", end='')
                current = current.next
            print(str(current.value) + " --> " + str(current.next))            
        else:
            print(str(current.value) + " --> " + str(current.next))

    def getItemAtPosition(self, position):
        """
            function to display the item at a given position
        """
        current = self.head
        if position > 0:
            for i in range(position+1):
                if i == position:
                    print(current.value)
                current = current.next
        elif position == 0:
            print(current.value)

    def append(self, new_item):
        """
            function to append an item to the end of the linked list
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_item
        else:
            self.head = new_item

    def insert(self, item, position):
        """
            function to insert an item at a given position in the linked list
        """
        current = self.head
        counter = 0
        if position > 0:
            while current and counter < position:
                if counter == position - 1:
                    item.next = current.next
                    current.next = item
                current = current.next
                counter+=1
        elif position == 0:
            item.next = self.head
            self.head = item
    
    def deleteItemAtPosition(self, position):
        """
            function to delete an item at a given position in the linked list
        """
        current = self.head
        previous = None
        if position > 0:
            for i in range(position+1):
                if i == position:
                    if current.next:
                        previous.next = current.next
                    else:
                        previous.next = None
                previous = current
                current = current.next
        elif position == 0:
            self.head = current.next

# Create Linked List
llist = LinkedList(Node('start'))

# Append data
llist.append(Node('1'))
llist.append(Node(2))
llist.append(Node(3))
llist.append(Node(4))
llist.append(Node(5))

# Insert data
llist.insert(Node(555),6)
llist.append(Node('end'))

# Print List
llist.printList()

# Print item value at specified position
llist.getItemAtPosition(6)

# Delete item at specified position
llist.deleteItemAtPosition(6)

llist.printList()
