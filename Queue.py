# Queue implementation using a linked list
# Node Class
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.previous = None

class Queue(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head:
            self.size = 1

    #  Function to print the entire Queue as a string
    def printQueue(self):
        current = self.head
        while current:
            print(str(current.value) + " -> ", end="")
            current = current.next
        print("*START*")

    # Function to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Function to get current size of the stack
    def getSize(self):
        return self.size

    # Function to add an item at the end of the queue
    def enqueue(self, item):
        if self.head:
            self.head.previous = item
            item.next = self.head
            self.head = item
            self.size+=1
        else:
            self.tail= item
            self.head = item
            self.size+=1

    # Remove and return an item from the start of queue
    def dequeue(self):
        print(self.getSize())
        if self.isEmpty():
            raise Exception("Dequeing from an empty Queue")
        else:
            removed = self.tail
            self.tail = removed.previous
            if removed.previous:
                removed.previous.next = None
            else:
                self.head = None
            self.size-=1
            return str(removed.value)
    

# Create a Queue
queue = Queue()

# Add items to start of queue
queue.enqueue(Node('head'))
queue.enqueue(Node(1))
queue.enqueue(Node(2))

# Display queue as a String
queue.printQueue()

# Remove items from the end of the queue and display them
print("removed " + queue.dequeue())
print("removed " + queue.dequeue())

queue.printQueue()
