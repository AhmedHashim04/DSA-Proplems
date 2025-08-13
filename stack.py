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
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = ['(',  '[' , '{', '}',')', ']']
        for i in s:
            if i in brackets[:3]:
                stk.append(i)
            elif i in brackets[3:]:
                if \
                (i == ')' and len(stk) > 0 and stk[-1] == "(") or \
                (i == ']' and len(stk) > 0 and stk[-1] == "[") or \
                (i == '}' and len(stk) > 0 and stk[-1] == "{")  :
                    stk.pop()
                else :return False
        if len(stk) == 0: return True
        else :return False

    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if len(stk)>0 and i == stk[-1]: 
                stk.pop()
            else :
                stk.append(i)
        return str(''.join(stk))


s = stack()

print(s.removeDuplicates("abbaca"))
