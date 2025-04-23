import ctypes

"""
Array Properties in C Language :
    -Fixed Size 
    -All elements is the same type
    -stored in continius inteveral places in memory 
    -Fixed elements dot swap dont change places
    -to access in element you spent 1 step
    -no append no len no check Bounds
    -if you want to append you need to create new array and copy old elements
""" 

class Array:
    def __init__(self, size,initial_values=None):
        self.size = size                    # user size
        self._capacity = max(16, 2*size)    # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = initial_values=None

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

    def right_rotate(self):
        """
        The function shifts every element 1 step towards the right.
            ● Assume the array content is: 0 1 2 3 4
            ● After a right rotation it will be: 4 0 1 2 3
                ○  the '4' has been rotated to the head of the array!

            ● No new array allocation/capacity expansion to occur
        """
        value = self.memory[self.size-1]

        for p in range(self.size - 1, 0 - 1, - 1):
            self.memory[p + 1] = self.memory[p]
        self.memory[0] = value

    def left_rotate(self):
        value = self.memory[0]
        for p in range(0, self.size):
            self.memory[p] = self.memory[p+1]
        self.memory[self.size-1] = value


    def right_rotate_steps(self,k):
        """
        The function shifts every element k step towards the right.
            ● Assume the array content is: 0 1 2 3 4
            ● After a right rotation it will be: 4 0 1 2 3
                ○  the '4' has been rotated to the head of the array!
                and repeated n times
        """
        k = k%len(self)
        for time in range(k):
            value = self.memory[self.size-1]
            for p in range(self.size - 1, 0 - 1, - 1):
                self.memory[p + 1] = self.memory[p]
            self.memory[0] = value
    def pop(self,pos=None):
        """
        Implement method pop( idx) to act similar to Python list
            ○ Index must be in range [-size to size-1], otherwise fail with error msg
        ■ pop index out of range
        ■ You can use assertion or throw an exception

        ● It returns the deleted value
        ● Remove this element from the array
        ● No new memory creation
        ● Code is very efficient if the removed element is the last
        one
        """
        if pos == None:
            temp = self.memory[self.size-1]
            self.memory = self.memory[:self.size-1]

        else:
                    
            if pos >= 0 :
                if self.size-1 < pos:
                    print ("pop index out of range")
                    return
                for i in range(self.size):
                    if i == pos:
                        temp = self.memory[i]
                        self.memory[pos] = None
                        break
                for o in range(pos,self.size):
                    self.memory[o]=self.memory[o+1]
            if pos < 0 :
                if self.size+pos < 0:
                    print ("pop index out of range")
                    return
                pos = pos + self.size
                for i in range(self.size):
                    if i == pos:
                        temp = self.memory[i]
                        self.memory[pos] = None
                        break
                for o in range(pos,self.size):
                    self.memory[o]=self.memory[o+1]

        self.size -= 1
        return temp
        
    def index_transposition(self,value):
        for p in range(self.size):
            if self.memory[p+1] == value:
                self.memory[p],self.memory[p+1] = self.memory[p+1],self.memory[p]
                return p
        if self.memory[0] == value:return 0
        return -1

class Array2D:
    def __init__(self, rows, columns,initial_values=None):
        """
        Initializes a 2D array with the specified number of rows and columns.

        Parameters:
        rows (int): The number of rows in the 2D array.
        column (int): The number of columns in each row of the 2D array.
        initial_value (optional): The initial value to fill in each position of the 2D array.
        """

        self.rows = rows
        self.columns = columns
        self.grid = Array(rows)
        for i in range(rows):
            self.grid[i] = Array(columns,initial_values) 

    def __getitem__(self, index):
        r, c = index[0], index[1]
        return self.grid[r][c]

    def __setitem__(self, index, value):
        r, c = index[0], index[1]
        self.grid[r][c] = value

    def __repr__(self):
        result = ''
        for i in range(self.rows):
            result += str(self.grid[i]) + '\n'
        return result

if __name__ == '__main__':

    # create 2x4 grid initialized to 0
    arr2d = Array2D(2, 4, 0)
    arr2d[(0, 2)] = 3
    arr2d[(1, 1)] = 5
    arr2d[(1, 3)] = 7
    print(arr2d)
    # 0, 0, 3, 0,
    # 0, 5, 0, 7,
    print(arr2d[(1, 3)])    # 7
