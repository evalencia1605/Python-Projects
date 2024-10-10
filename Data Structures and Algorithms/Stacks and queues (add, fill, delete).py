class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty!!"
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value
    
    def delete_value(self, value):
        if self.is_empty():
            return "Stack is empty!!"
        
        current = self.top
        previous = None

        while current and current.value != value:
            previous = current
            current = current.next

        if current is None:
            return f"Value {value} not in stack!"
        
        if previous is None:
            self.top = current.next
        else:
            previous.next = current.next


    def fill_stack(self, values):
        if isinstance(values, list):
            for value in reversed(values):
                self.push(value)
        else:
            return "Please provide a list of values"
        

    def display(self):
            current = self.top
            stack_values = []
            while current:
                stack_values.append(current.value)
                current = current.next
            return stack_values

stack = Stack()    

stack.fill_stack([20, 30, 66])
stack.push(21)
stack.push(31)
stack.push(28)

stack.delete_value(30)

print(stack.display())


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!!"
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def delete_value(self, value):
        if self.is_empty():
            return "Queue is empty!!"

        current = self.front
        previous = None

        while current and current.value != value:
            previous = current
            current = current.next

        if current is None:
            return f"Value {value} not in queue!"

        if previous is None:
            self.front = current.next
            if self.front is None:  
                self.rear = None
        else:
            previous.next = current.next
            if current == self.rear:  
                self.rear = previous

    def fill_queue(self, values):
        if isinstance(values, list):
            for value in values:
                self.enqueue(value)
        else:
            return "Please provide a list of values"

    def display(self):
        current = self.front
        queue_values = []
        while current:
            queue_values.append(current.value)
            current = current.next
        return queue_values

queue = Queue()

queue.fill_queue([20, 30, 66])
queue.enqueue(21)
queue.enqueue(31)
queue.enqueue(28)

queue.delete_value(30)

print(queue.display())