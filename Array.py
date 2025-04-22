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

    def __init__(self,size):
        self.expand_times = 0
        self.size = size
        self._capacity = 16 # 16 is actual size of memory

        array  = ctypes.py_object * self._capacity
        self.memory = array()

        for i in range(self._capacity):
            self.memory[i] = None



    def __len__(self):
        return self.size
    
    def __getitem__(self,index):
        return self.memory[index]

    def __setitem__(self,index,value):
        self.memory[index] = value
    
    def __repr__(self):
        result = 'arr() {'
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        
        result = result[:len(result)-2]
        result += '}'
        return result

    def append(self,value,capacity_trick=0):
        # Start Capacity trick
        if capacity_trick :
            if self.size == self._capacity:
                print(f"Capacity now is : {self._capacity}")
                self._capacity *= 2
                self.expand_times += 1
                print(f'Expand capacity to {self._capacity}')

                #Create new array
                new_memory = (ctypes.py_object * self._capacity)()

                # Copy elements
                for i in range(self.size):
                    new_memory[i] = self.memory[i]
                
                self.memory = new_memory

        else:
            if self.size == self._capacity:
                print(f"Capacity now is : {self._capacity}")
                self._capacity += 1
                self.expand_times += 1
                print(f'Expand capacity to {self._capacity}')
                #Create new array
                new_memory = (ctypes.py_object * self._capacity)()

                # Copy elements
                for i in range(self.size):
                    new_memory[i] = self.memory[i]
                
                self.memory = new_memory
    
        self.memory[self.size] = value
        self.size += 1
        print(f"Capacity now is : {self._capacity}")



arr = Array(16)

for i in range(arr.size):
    arr.memory[i] = i+1



for i in range(10 ** 4):
    arr.append(i,1)
    # arr.append(i)

print(arr.expand_times)

print(len(arr))
"""
1/10
3/100
6/1000

"""