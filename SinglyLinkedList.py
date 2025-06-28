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

    def __len__(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    
    def insertFront(self,value):
        newNode = node(value)
        newNode.next = self.head
        self.head = newNode

    def deleteFront(self):
        self.head = self.head.next

    def get_item(self, item):
        current = self.head
        for pos in range(1, len(self) + 1):  #O(N)
            if current.data == item:
                return pos
            current = current.next
        return None

    def get_nth(self, pos): #O(n)
        if pos <= 0:
            return "nothing is orderd"
        
        i,n = 1,self.head
        while n:
            if i == pos : return n.data
            n,i = n.next,i+1
        return "the lenth isn,t big as ur pos as"

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

    def get_nth_from_back_recursive(self, cur, pos):
        def recursive_helper(node, pos):
            if node is None:
                return 0, None
            idx, result = recursive_helper(node.next, pos)
            idx += 1
            if idx == pos:
                return idx, node.data
            return idx, result

        _, result = recursive_helper(cur, pos)
        return result

    def improved_search(self,item):
        current, prev = self.head, None
        if self.head is None: return None
        if self.head.data == item: return 1
        if not self.head.next: return None

        for pos in range(1, len(self) + 1):  #O(N)
            if current.data == item:
                if not prev :
                    return pos
                current, prev = prev, current
                return pos
            prev,current = current, current.next

        return None

    def swap_pairs(self):
        if not self.head or not self.head.next: return
        
        current = self.head
        while current and current.next:
            temp = current.data
            current.data = current.next.data
            current.next.data = temp
            current = current.next
        return (self)

    def debug_verify_data_integrity(self):
        if len(self) == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.tail is not None
        assert self.tail.next is None

        if len(self) == 1:
            assert self.head == self.tail
        elif len(self) == 2:
            assert self.head.next == self.tail
        else:
            actual_lst_len = 0
            temp_head = self.head

            while temp_head is not None:
                temp_head = temp_head.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert len(self) == actual_lst_len
            assert len(self) == len(self.debug_data)


def identicalLinkedLists(L1, L2):
    """
    Checks if 2 lists have identical data:
        ○ Each list must be the same length
        ○ The value of a node in one list must
            match the value of its corresponding node in the other list
    """

    cur1 = L1.head
    cur2 = L2.head
    while cur1 is not None and cur2 is not None:
        if cur1.data != cur2.data:
            return False
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1 is None and cur2 is None


LL1 = SinglyLinkedList([1,2,3,4,5])
LL2 = SinglyLinkedList([1,2,3])

# print(identicalLinkedLists(L1=LL1,L2=LL2))
# print(LL1.improved_search(5))
print(LL1.swap_pairs())