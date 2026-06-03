from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next: Optional['Node'] = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None


    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def delete(self, val):

        temp = self.head
        prev = None

        while temp:

            if temp.val == val:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Node not found")


    def traversal(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)

print("Before deletion: ",end=" ")
sll.traversal()

sll.delete(30)

print("After deletion: ", end=" ")
sll.traversal()