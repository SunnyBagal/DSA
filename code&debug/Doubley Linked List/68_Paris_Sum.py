class Node:
  def __init__(self, val):
    self.next = None
    self.prev = None
    self.val = val

class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_head(self,val):
    new_node = Node(val)
    if not self.head:
      self.head = self.tail = new_node
      return
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    
  def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ⇄ ")
            temp = temp.next
        print("None")

  def sumPairs(self, target):
    temp1 = self.head
    result = []
    while temp1 is not None:
      temp2 = temp1.next
      while temp2 is not None:
        if temp1.val + temp2.val == target:
          result.append([temp1.val, temp2.val])
        temp2 = temp2.next 
      temp1 = temp1.next
    return result
  
  def sumOfParis(self, target):
    my_set = set()
    temp = self.head
    res = []
    while temp is not None:
      remaining = target - temp.val
      if remaining in my_set:
          res.append([remaining, temp.val])
      my_set.add(temp.val)
      temp = temp.next
    return res
        

  def sumOfPairs(self, target):
    res = []
    first = self.head
    last = self.tail
    while first is not None and last is not None and first != last and last.next != first:
        curr_sum = first.val + last.val
        if curr_sum == target:
            res.append([first.val, last.val])
            first = first.next
            last = last.prev
        elif curr_sum < target:
            first = first.next
        else:
            last = last.prev

    return res
  

dll = DoublyLinkedList()

# Insert values (IMPORTANT: insert in reverse to keep sorted order)
values = [9, 7, 5, 3, 1]  # final list: 1 ⇄ 3 ⇄ 5 ⇄ 7 ⇄ 9
for v in values:
    dll.insert_at_head(v)

print("Doubly Linked List:")
dll.traverse_forward()

target = 10
print(f"\nPairs with sum {target}:")
print(dll.sumOfPairs(target))
print(dll.sumOfParis(target))
print(dll.sumPairs(target))
        