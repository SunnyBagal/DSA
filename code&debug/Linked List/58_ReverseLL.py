class Node :
  def __init__(self,val):
    self.head = None
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    new_Node = Node(val)

    if self.head is None:
      self.head = new_Node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_Node

  
  def Reversal(self):
    temp = self.head
    prev = None
    while temp is not None:
      front = temp.next
      temp.next = prev
      prev = temp
      temp = front 

    return prev

