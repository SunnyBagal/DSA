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

  def reversal(self):
    temp = self.head
    stack = []
    while temp is not None:
      stack.append(temp.val)
      temp = temp.next
    temp = self.head
    while temp is not None:
      e = stack.pop()
      temp.val = e
      temp = temp.next

  def reversalOptimal(self):
    if not self.head:
        return
    current = self.head
    prev = None
    self.tail = self.head
    while current is not None:
        front = current.next
        current.next = prev
        current.prev = front
        prev = current
        current = front
    # update head
    self.head = prev
  
  #~ TC: O(N)
  #~ SC: O(1)

# -------- TESTING --------

dll = DoublyLinkedList()

# Insert elements
dll.insert_at_head(5)
dll.insert_at_head(4)
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)

print("Original list (forward):")
temp = dll.head
while temp:
    print(temp.val, end=" ⇄ ")
    temp = temp.next
print("None")

# Reverse using stack
dll.reversalOptimal()

print("\nAfter reversal (forward):")
temp = dll.head
while temp:
    print(temp.val, end=" ⇄ ")
    temp = temp.next
print("None")


    
