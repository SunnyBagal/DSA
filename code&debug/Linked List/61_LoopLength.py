class Node:
  def __init__(self,val):
    self.next = None
    self.val = val

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self,val):
    new_node = Node(val)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node

  def traversal(self):
    if self.head is None:
      print("Sll is empty")
    else:
      current_head = self.head
      while current_head is not None:
        print(current_head.val, end=" ")
        current_head = current_head.next
      print()


  def loopLength(self):
    temp = self.head
    my_dict = {}
    travel = 0
    while temp is not None:
      if temp in my_dict:
        return travel - my_dict[temp]
      else:
        my_dict[temp] = travel 
        travel += 1
        temp = temp.next
    return 0
  #~ TC: O(N)
  #~ SC: O(N)

  def optimalLoopLength(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        slow = slow.next
        count = 1
        while slow != fast :
          slow = slow.next 
          count += 1
        return count 
    return 0

  #~ TC: O(N)
  #~ SC: O(1)


sll = SinglyLinkedList()
sll.append(5)
sll.append(9)
sll.append(1)
sll.append(7)
sll.append(6)
sll.append(1)
sll.append(9)
sll.append(2)
sll.append(8)
sll.traversal()

#*--------------------------
tp = sll.head
third = tp.next.next
while tp.next is not None:
  tp = tp.next
tp.next = third
#*--------------------------

print(f'after cycle: {sll.loopLength()}')
print(sll.optimalLoopLength())