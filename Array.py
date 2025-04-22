import ctypes

"""
Array Properties in C Language :
    -Fixed Size 
    -All elements is the same type
    -stored in continius inteveral places in memory 
    -Fixed elements dot swab dont change places
    -to access in element you spent 1 step
    -no append no len no check Bounds
    -if you want to append you need to create new array and copy old elements
""" 

class Array:
    def __init__(self, size):
        self.size = size                    # user size
        self._capacity = max(16, 2*size)    # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        # Double the actual array size
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        # create a new array of _capacity
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory

    def append(self, value):
        if self.size == self._capacity:
            self.expand_capacity()
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

    def insert(self, idx, value):
        if self.size == self._capacity:
            self.expand_capacity()
        for i in range(self.size-1,idx-1,-1):
            self.memory[i+1]=self.memory[i]
        self.memory[idx] = value
        self.size += 1


array = Array(0)
array.append(56)
array.append('hello')
print(array)
#56, hello,
array.insert(0, 'A0')
print(array)
# A0, 56, hello,
array.insert(2, 'A2')
print(array)
# A0, 56, A2, hello,
array.insert(1, -9)
print(array)
# A0, -9, 56, A2, hello,