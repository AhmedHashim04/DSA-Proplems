class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, list: list):
        self.head = None
        if list:
            self.head = node(list[0])           # Time : O(N), Memory : O(N)
            current = self.head
            for value in list[1:]:
                current.next = node(value)
                current.next.prev = current
                current = current.next
        
    @staticmethod
    def _link(first=None,second=None):
        if first:
            first.next = second
        if second:
            second.prev = first

    @property
    def getTail(self):
        current = self.head
        while current.next:
            current = current.next
        return current
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return str(result)
    
    
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def append(self, value):
        new_node = node(value)
        if self.head and self.head.next is None:
            self.head = new_node
            return
        self._link(self.getTail, new_node)

    def prepend(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            return
        self._link(new_node, self.head)
        self.head = new_node
    
    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                self._link(current.prev, current.next)
                return
            current = current.next
    def delete_tail(self):
        self._link(self.getTail.prev, None)
    
    def delete_head(self):
        self._link(None, self.head.next)
        self.head = self.head.next

    def insert_after(self, value, after):
        current = self.head
        while current:
            if current.value == after:
                self._link(current, node(value))
                self._link(current.next, current.next.next)
                return
            current = current.next

    def insert_sorted(self,value):
        if self.head is None or self.head.value >= value:
            self.prepend(value)
            return
        current = self.head
        while current.next and current.next.value < value:
            current = current.next
        self._link(current, node(value))
        self._link(current.next, current.next.next)

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        headPoint = self.head
        tailPoint = self.getTail

        while headPoint != tailPoint and headPoint.prev != tailPoint:
            if headPoint.value != tailPoint.value:
                return False
            headPoint = headPoint.next
            tailPoint = tailPoint.prev

        return True

    def middle_value(self):
        headPtr=self.head
        tailPtr=self.getTail
        while headPtr!=tailPtr and headPtr.next!=tailPtr:
            headPtr = headPtr.next
            tailPtr = tailPtr.prev

        return headPtr.value

    def middle_with__tortoise_and_the_hare(self):
        slowPtr = self.head
        fastPtr = self.head

        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        return slowPtr

    def swap_kth_nodes(self,k):
        if k <= 0 or k > len(self):
            return  
        
        headPtr = self.head
        tailPtr = self.getTail
        c = 0

        while c != k:
            headPtr = headPtr.next
            tailPtr = tailPtr.prev
            c += 1
            
        headPtr.next, headPtr.prev, tailPtr.next, tailPtr.prev = \
        tailPtr.next, tailPtr.prev, headPtr.next, headPtr.prev

        l

lista = DoublyLinkedList([1,2,3,4,5,6,7,8,9,10])
print(lista)
print(lista.is_palindrome())

print(lista.middle_value())