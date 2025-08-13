class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def reverse_num(self,num):
        while num > 0:
            self.push(num%10)
            num = num//10
            
        reversed_num = 0
        place = 1
        while self.items:
            reversed_num += self.pop() * place
            place *= 10

        return reversed_num        


s = stack()
print(s.reverse_num(123400))