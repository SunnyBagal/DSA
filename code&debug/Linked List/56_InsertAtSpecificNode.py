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
      current = self.head

      while current.next is not None:
        current = current.next

      current.next = new_node


  def insert_at(self, val, position):
    new_node = Node(val)

    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return

    current = self.head
    prev_node = None
    count = 0

    while current is not None and count < position:
      prev_node = current
      current = current.next
      count += 1

    if prev_node is None:
      print("Position out of range")
      return

    prev_node.next = new_node
    new_node.next = current


