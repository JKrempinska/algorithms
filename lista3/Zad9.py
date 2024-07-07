from Zad5 import Queue

class Stack:
    
    def __init__(self):
        self.queue = Queue()
        self.top_e = None

    def push(self,e):
        self.queue.enqueue(e)
        self.top_e = e

    def pop(self):
        if self.queue.is_empty():
            raise ValueError('Stack is empty')
        else:
            for _ in range(self.queue.__len__()-1):
                first = self.queue.dequeue()
                self.queue.enqueue(first)
                self.top_e = first
            e = self.queue.dequeue()
            return e

    def top(self):
        return self.top_e


