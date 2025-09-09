q = []
front = 0
back = 0

def de(q):
    if len(q)== 0 :
        q[front] = -1
    else:
        
    
    front += 1

    
def en(q,i): #time = O(1) memory = O(n) 
    if len(q)== 0 :
        q[0] = i
    else:
        q[back] = i 

    back += 1
    
def display(q):
    pass