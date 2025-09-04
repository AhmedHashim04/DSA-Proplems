class Queue:
    def __init__(self, queue_initial_values = [], queue_capacity = 5):
        self.Q = queue_initial_values
        self.rear = len(queue_initial_values)
        self.front = 0
        self.capacity = queue_capacity
        self.size = len(queue_initial_values)

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

class CircularQueue(Queue):

    def enqueue(self, item):
        if self.Q[self.rear] == -1 or self.size < self.capacity:
            self.Q[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
            return True