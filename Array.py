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

        array = ctypes.py_object * size
        self.size = size
        self.memory = array()

    def __len__(self):
        return self.size
    def __getitem__(self,index):
        return self.memory[index]

    def __setitem__(self,index,value):
        self.memory[index] = value
    
    def append(self,value):
        # capacity trick
        pass