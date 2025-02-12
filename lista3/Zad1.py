import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0 
        self._capacity = 1 
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n 

    def __getitem__(self,k):
        if not 0 <= k < self._n: 
            raise IndexError('invalid index')
        return self._A[k] 

    def append(self,obj):
        if self._n == self._capacity: 
            self._resize(2*self._capacity) 
        self._A[self._n] = obj 
        self._n += 1 

    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n): 
            B[k] = self._A[k] 
        self._A = B 
        self._capacity = c 

    def _make_array(self,c): 
        return (c*ctypes.py_object)()
    
    def insert(self,k,value):
        if self._n == self._capacity: 
            self._resize(2*self._capacity)
        B = self._make_array(self._capacity)
        for i in range(self._n):
            if i<k:
                B[i] = self._A[i]
            elif i>=k:
                B[i+1] = self._A[i]
        B[k] = value
        self._A = B
             
    def remove(self,value):
        B = self._make_array(self._capacity)
        for i in range(self._n):
            if self._A[i] == value:
                j = i
                break
        for i in range(self._n-1):
            if i<j:
                B[i] = self._A[i]
            elif i>=j:
                B[i] = self._A[i+1]
        self._A = B

    def expand(self,seq):
        for i in range(len(seq)):
            if self._n == self._capacity: 
                self._resize(2*self._capacity) 
            self._A[self._n] = seq[i] 
            self._n += 1

    def __str__(self):
        text = '|'
        for i in range(self._capacity):
            if i<self._n:
                text += str(self._A[i]) + '|'
            else:
                text += ' |'
        return text 

mylist = DynamicArray()
mylist.expand([1,2,3,4,5,6,7,8,9])
print(mylist)

        