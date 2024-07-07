class Empty(Exception):
    pass
class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next' 

        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
import time
import matplotlib.pyplot as plt

n_list = [x*100 for x in range(1,100)]
times_push = []
times_pop = []

for i in range(len(n_list)): 
    times_n = 0
    for _ in range(100): 
        s = LinkedStack()
        start = time.perf_counter()
        for _ in range(n_list[i]):
            s.push(1)
        end = time.perf_counter()
        tn = end - start
        times_n += tn
    times_push.append(times_n/100)

for i in range(len(n_list)): 
    times_n = 0
    for _ in range(100): 
        s = LinkedStack()
        for _ in range(n_list[i]):
            s.push(1)
        start = time.perf_counter()
        s.pop()
        end = time.perf_counter()
        tn = end - start
        times_n += tn
    times_pop.append(times_n/100)



plt.plot(n_list, times_push, label='push')
plt.plot(n_list, times_pop, label='push')
plt.legend()
plt.show()
    

