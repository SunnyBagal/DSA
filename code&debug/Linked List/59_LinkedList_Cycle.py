from typing import Optional
class Node:
  def __init__(self,val):
    self.next: Optional['Node'] = None
    self.val = val

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def Append(self, val):
    new_node = Node(val)

    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node


  def isCycle(self):
    temp = self.head
    my_set = set()

    while temp is not None:
      if temp in my_set:
        return True
      else:
        my_set.add(temp)
        temp = temp.next 
    return False
  
  def isCycleOptimal(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True 
    return False

    #~ TC: O(N)
    #~ SC: O(1)


  
sll = SinglyLinkedList()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.Append(40)

print("Cycle present:", sll.isCycle())
print("Cycle present:", sll.isCycleOptimal())


temp = sll.head
second = temp.next

while temp.next is not None:
    temp = temp.next

temp.next = second

print("Cycle present:", sll.isCycle())
print("Cycle present:", sll.isCycleOptimal())


#~ TC: O(N)
#~ SC: O(N) = set ke andar sab to aa hi rahe hai 

