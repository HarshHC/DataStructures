# Implementing stack using a linked list
# Node Class
class Node(object):
    # Initialize node with value
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack Class
class Stack(object):
    # Initializing stack with head value and setting default size to 1
    def __init__(self, head=None):
        self.head = head
        if head: 
            self.size = 1 
        else: 
            self.size = 0

    # Function to print the entire stack as string
    def printStack(self):
        current = self.head
        while current:
            print(str(current.value) + " -> ", end="")
            current = current.next
        print(str(current))

    # Function to get current size of the stack
    def getSize(self):
        return self.size
    
    # Function to check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Function to get the top item in the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        print(self.head.value)
    
    # function to add an item to the top of the stack
    def push(self, item):
        item.next = self.head
        self.head = item
        self.size+=1

    # function to remove an item from the top of the stack
    def pop(self):
        if self.isEmpty():
             raise Exception("Popping from an empty stack")
        self.head = self.head.next
        self.size-=1

# Create a Stack
stack = Stack()

# Print current stack size
print(stack.getSize())

# Push Data to the top
stack.push(Node('head'))
stack.push(Node(1))
stack.push(Node(2))
stack.push(Node(3))
stack.push(Node(4))
stack.push(Node(5))

# Display the stack
stack.printStack()

# Pop Data from the top
stack.pop()
stack.printStack()

# Peek top item
stack.peek()