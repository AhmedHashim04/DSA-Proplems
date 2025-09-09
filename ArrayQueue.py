
import ctypes
class Array:
    def __init__(self, capacity):
        self.size = 0
        self._capacity = capacity
        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

    def append(self, value):
        if self.size == self._capacity:
            return
        self.memory[self.size] = value
        self.size += 1

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]  # Is valid idx?

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result
    
class Queue:
    def __init__(self, initial_values=[]):
        self.queue = Array(5)
        self.memory = self.queue.memory
        self.size = 0
        self.capacity = self.queue._capacity
        self.rear = 0
        self.front = 0
        if len(initial_values) > 0:
            for i in initial_values:
                self.enqueue(i)
        print(repr(self))

    def _next(self, value):
        return (value + 1) % self.capacity

    def __repr__(self):
        result = ''
        count = 0
        curr = self.front
        while count < self.size:
            result += str(self.memory[curr]) + ', '
            curr = self._next(curr)
            count += 1
        return result.strip(', ')

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.memory[self.front] = -1
        self.front = self._next(self.front)
        self.size -= 1

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is Full")
        self.memory[self.rear] = value
        self.rear = self._next(self.rear)
        self.size += 1

class StackFromQueue:
    def __init__(self,initials):
        self.queue = Queue(initials)

    def push(self,value):
        self.queue.enqueue(value)


    # def pop(self):
    #     if self.queue.is_empty():
    #         raise Exception("Stack is empty")
    #     count = 0
    #     curr = self.queue.front
    #     while count < self.queue.size:
    #         curr = self.queue._next(curr)
    #         count += 1
    #     self.queue[curr] = -1
    #     self.queue.rear -= 1
    #     self.queue.size -= 1



    def pop(self):
        if self.queue.is_empty():
            raise Exception("Stack is empty")
        # Find the index of the last element
        last_idx = (self.queue.rear - 1 + self.queue.capacity) % self.queue.capacity
        value = self.queue.memory[last_idx]
        self.queue.memory[last_idx] = -1
        self.queue.rear = last_idx
        self.queue.size -= 1
        return value


S=StackFromQueue([1,2,53,6])
S.pop()
print(S.queue)
