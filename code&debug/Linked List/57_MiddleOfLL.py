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

    temp = self.head
    while temp.next is not None:
      temp = temp.next

    temp.next = new_node


  def middle_Value(self):
    # n = 0
    # temp = self.head

    # while temp is not None:
    #   n += 1
    #   temp = temp.next

    # temp = self.head

    # for i in range(n//2):
    #   temp = temp.next

    # return temp.val

    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
    return slow.val
  

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print(sll.middle_Value())