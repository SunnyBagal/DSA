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

  def append_insertAtEnd(self,val):
    new_node = Node(val)
    if not self.head:
      self.head = self.tail = new_node
      return
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
      new_node.prev = current 

  def insert_at_tail(self, val):
    new_node = Node(val)
    if self.tail is None:
      self.head = self.tail = new_node
      return
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    
  def insert_in_Between(self,val, pos):
    new_node = Node(val)
    if pos == 0:
      self.insert_at_head(val)
      return 
    
    current = self.head
    count = 0 
    while current and count < pos - 1:
      current = current.next
      count += 1
    if current is None:
      return
    
    new_node.next = current.next
    new_node.prev = current
    if current.next:
      current.next.prev = new_node
    current.next = new_node


  def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ⇄ ")
            temp = temp.next
        print("None")

  def traverse_backwards(self):
    temp = self.tail
    while temp:
      print(temp.val, end=" ⇄ ")
      temp = temp.prev
    print("None")

  def delete_head(self):
    if not self.head:
        return
    if self.head == self.tail:
        self.head = self.tail = None
        return
    self.head = self.head.next
    self.head.prev = None

  def delete_last(self):
    if not self.tail:
        return

    if self.head == self.tail:
        self.head = self.tail = None
        return

    self.tail = self.tail.prev
    self.tail.next = None
  
  def delete_in_Between(self, pos):
    if not self.head:
        return
    if pos == 0:
        self.delete_head()
        return
    current = self.head
    count = 0
    while current and count < pos:
        current = current.next
        count += 1
    if not current:
        return
    if current == self.tail:
        self.delete_last()
        return
    else:
      current.prev.next = current.next
      current.next.prev = current.prev

# -------- TESTING DOUBLY LINKED LIST --------

dll = DoublyLinkedList()

print("Initial list (should be empty):")
dll.traverse_forward()
dll.traverse_backwards()

# Insert at head
print("\nInsert at head:")
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)
dll.traverse_forward()
dll.traverse_backwards()

# Insert at tail
print("\nInsert at tail:")
dll.insert_at_tail(4)
dll.insert_at_tail(5)
dll.traverse_forward()
dll.traverse_backwards()

# Insert in between
print("\nInsert at position 2 (value = 99):")
dll.insert_in_Between(99, 2)
dll.traverse_forward()
dll.traverse_backwards()

# Delete head
print("\nDelete head:")
dll.delete_head()
dll.traverse_forward()
dll.traverse_backwards()

# Delete last
print("\nDelete last:")
dll.delete_last()
dll.traverse_forward()
dll.traverse_backwards()

# Delete in between
print("\nDelete at position 2:")
dll.delete_in_Between(2)
dll.traverse_forward()
dll.traverse_backwards()