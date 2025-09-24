class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    @property
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

    def asteroidCollision(self, asteroids):
        while asteroids:
            if self.isEmpty or (self.items[-1] < 0 and asteroids[0] > 0):
                self.push(asteroids.pop(0))
            elif self.items[-1] > 0 > asteroids[0]:

                if abs(self.items[-1]) > abs(asteroids[0]):
                    asteroids.pop(0)
                elif abs(self.items[-1]) < abs(asteroids[0]):
                    self.items.pop()
                elif abs(self.items[-1]) == abs(asteroids[0]):
                    self.items.pop()
                    asteroids.pop(0)
                else:
                    asteroids.pop(0)
    
            else:self.push(asteroids.pop(0))


        return self.items
    
    def manual_stack(self, num):
        while num > 0:
            self.push(num)
            num -= 1

        while not self.isEmpty:
            print(self.pop(), end=" ")

    def scoreOfParentheses(self,s: str) -> int:
        stack = [0]  
        for ch in s:
            print(stack)
            if ch == "(":stack.append(0)  

            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()

    def dailyTempretures(self,temperatures = [73, 74, 75, 71, 69, 72, 76, 73]): #REVIEW it 

        n = len(temperatures)
        answer = [0] *n
        stk = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < curr_temp:
                prev_day = stk.pop()
                answer[prev_day] = curr_day - prev_day
            stk.append(curr_day)

        return answer
s = stack()
print(enumerate([1,2,58,88]))
# print(s.dailyTempretures())

class QueueUsing2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise Exception("Queue is empty")
        return self.stack2.pop()