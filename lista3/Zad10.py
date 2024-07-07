class Queue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def show(self):
        print(self.stack_1)
        print(self.stack_2)
    
    def enqueue(self, e):
        self.stack_1.append(e)
        
    def dequeue(self):
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            raise ValueError('Queue is empty')
        
        elif len(self.stack_2) == 0 and len(self.stack_1) > 0:
            while len(self.stack_1) != 0:
                e = self.stack_1.pop(0)
                self.stack_2.append(e)
                return self.stack_2.pop(0)
        
        else:
            self.stack_2.pop()



        
