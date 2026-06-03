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
    else:
      current_head = self.head
      while current_head.next is not None:
        current_head = current_head.next
      current_head.next = new_node


  def traversal(self):
    if self.head is None:
      print("Sll is empty")
    else:
      current_head = self.head

      while current_head is not None:
        print(current_head.val, end=" ")
        current_head = current_head.next
      print()


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll.traversal()