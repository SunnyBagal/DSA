class Node:
  def __init__(self, val):
    self.next = None
    self.prev = None
    self.val = val 

class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
  
  def traverse_forward(self):
    temp = self.head
    while temp:
      print(temp.val, end=" ⇄ ")
      temp = temp.next
    print("None")
  
  def insert_atTail(self, val):
    new_node = Node(val)
    if self.tail is None:
      self.head = self.tail = new_node
      return
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    
  def remove_Dupes(self):
    temp = self.head

    while temp and temp.next:
        if temp.val == temp.next.val:
            # duplicate found
            nxt = temp.next
            temp.next = nxt.next

            if nxt.next:
                nxt.next.prev = temp
            else:
                self.tail = temp  # update tail if needed

        else:
            temp = temp.next
    return


# 🔥 TESTING

dll = DoublyLinkedList()

values = [1,1,1,3,4,5,6,6,6,7]
for v in values:
    dll.insert_atTail(v)

print("Original List:")
dll.traverse_forward()

# Call your function
dll.remove_Dupes()

print("\nAfter Removing Duplicates:")
dll.traverse_forward()
