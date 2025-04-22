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

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self._capacity):  # initialize new memory with None
            new_memory[i] = None

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
        """
        ● In the lecture, we implement insert function to allow only integer indices in the
        range [0, size-1]
        ● However, list in Python allows negative indexing
        ● Change the code to allow negative integer indexing
            ○ In practice, the user may also make mistakes by passing a float or a wrong data type
            ○ Handling these mistakes is out of our scope
        ● Change your code to work according to the list as follows:
        """
        if self.size == self._capacity:
            self.expand_capacity()
        if idx > self.size:
            self.append(value)
            return
        if idx >= 0 :
            for p in range(self.size - 1, idx - 1, - 1):
                self.memory[p + 1] = self.memory[p]
            self.memory[idx] = value

        else :
            for p in range(self.size-self._capacity-1, (idx+self.size-self._capacity-1), - 1):
                self.memory[p + 1] = self.memory[p]
            self.memory[self.size-self._capacity+idx] = value

        self.size += 1
# -3 idx
# size = 4
# total -16

def test_insert():
    array = Array(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    # 1, 2, 3, 4
    array.insert(-1, -10)
    print(array)  # 1, 2, 3, -10, 4,

    array.insert(-2, -20)
    print(array)  # 1, 2, 3, -20, -10, 4,

    array.insert(-3, -30)
    print(array)  # 1, 2, 3, -30, -20, -10, 4,

    array.insert(-4, -40)
    print(array)  # 1, 2, 3, -40, -30, -20, -10, 4,

    array.insert(-5, -50)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 4,

    array.insert(8, 80)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4,

    array.insert(20, 90)
    print(array)  # 1, 2, 3, -50, -40, -30, -20, -10, 80, 4, 90,
test_insert()

