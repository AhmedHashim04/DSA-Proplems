class Queue:
    def __init__(self, queue_initial_values = [], queue_capacity = 5):
        self.Q = queue_initial_values
        self.rear = len(queue_initial_values)
        self.front = 0
        self.capacity = queue_capacity
        self.size = len(queue_initial_values)


    def _next(self, pos):
        pos += 1
        if pos == self.capacity:
            pos = 0
        return pos
        # return (pos + 1) % size	#  Or shorter way

    def _prev(self, pos):
        pos -= 1
        if pos == -1:
            pos = self.capacity - 1
        return pos
        # return (pos  - 1 + size) % size	#  Or shorter way


    def enqueue(self, item):
        if self.is_full():
            return False
        self.Q[self.rear] = item
        self.rear += 1
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.Q[self.front]
        self.front += 1
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def rear(self):
        return self.rear

    def front(self):
        return self.front

    def display(self):
        print(f"Front {self.front} - rear {self.rear}", end = '\t')

        if self.is_full():
            print("FULL", end='')
        elif self.is_empty():
            print("EMPTY\n")
            return

        print("")
        cur = self.front

        for step in range(self.size):
            print(self.Q[cur], end=" ")
            cur = self._next(cur)
        print("")


class CircularQueue(Queue):

    def enqueue(self, item):
        if self.Q[self.rear] == -1 or self.size < self.capacity:
            self.Q[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
            return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.Q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def reverse_dequeue(self):
        if self.is_empty():
            return None
        self.rear = self.rear-1
        item = self.Q[self.rear]
        self.Q[self.rear] = None
        self.size -= 1
        return item

    def reverse_enqueue(self,item):
        self.Q[self.front] = item
        

class Stack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.enqueue(item)

    def pop(self):
        if self.queue.is_empty():
            return None
        # Move all elements except the last one to the front
        while self.queue.size > 1:
            self.queue.enqueue(self.queue.dequeue())
        return self.queue.dequeue()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()

    def display(self):
        self.queue.display()