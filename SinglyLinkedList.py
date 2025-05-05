class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, list: list):
        self.head = None
        if list:
            self.head = node(list[0])           # Time : O(N), Memory : O(N)
            current = self.head
            for value in list[1:]:
                current.next = node(value)
                current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __repr__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " -> "
            current = current.next
        return result + "None"

    def insertFront(self,value):
        newNode = node(value)
        newNode.next = self.head
        self.head = newNode
    def deleteFront(self):
        self.head = self.head.next

    def __len__(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    
    def get_nth_from_back(self,pos):
        """
        Retrieves the element at the given position from the back of the list.

        """
        if self.head:
            if pos > len(self) or pos <= 0 :
                return None
            idx = 0
            current = self.head
            while idx != len(self)-pos :
                current = current.next
                idx += 1

            return f"element: {current.data} in pos: {pos}"

            

LL = SinglyLinkedList([1,2,3,4,5])
LL.insertFront(0)
# LL.deleteFront()
print(LL)
print(LL.get_nth_from_back(6))