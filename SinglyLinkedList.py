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

LL = SinglyLinkedList([1,2,3,4,5])
LL.insertFront(0)
LL.deleteFront()
print(LL)