class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    # Push element x to the back of queue
    def push(self, x):
        self.input.append(x)

    # Removes the element from the front of queue
    def pop(self):
        self.peek()
        return self.output.pop()

    # Get the front element
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    # Returns whether the queue is empty
    def empty(self):
        return not self.input and not self.output