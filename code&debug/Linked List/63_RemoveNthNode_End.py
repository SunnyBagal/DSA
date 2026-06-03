class Node:
  def __init__(self, val):
    self.next = None
    self.val = val

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
  
  def removeNth_fromEnd(self, n):
    length = 0
    temp = self.head
    while temp is not None:
      length += 1
      temp = temp.next
    if length == n:
      new_head = self.head.next 
      del(self.head)
      return new_head
    
    stop = length - n
    temp = self.head
    count = 1
    while count < stop :
      temp = temp.next
      count += 1
    temp.next = temp.next.next
    return self.head

  def removeOptimal(self, n):
    slow = self.head
    fast = self.head
    for _ in range(n):
      fast = fast.next
    if fast == None:
      return self.head.next
    
    while fast.next is not None:
      slow = slow.next
      fast = fast.next

    slow.next = slow.next.next

    return self.head
    


# Helper function to print values (better than printing node objects)
def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" → ")
        temp = temp.next
    print("None")

# Create list
sll = SinglyLinkedList()

# Insert values
values = [10, 20, 30, 40, 50]
for v in values:
    sll.append(v)

print("Original list:")
print_list(sll.head)

# -------------------------------
# Test removeNth_fromEnd
# -------------------------------
print("\nTesting removeNth_fromEnd (remove 2nd from end):")
new_head = sll.removeNth_fromEnd(2)
print_list(new_head)
#~ TC: O(2N)
#~ SC: O(1)
# -------------------------------
# Rebuild list (important!)
# -------------------------------
sll = SinglyLinkedList()
for v in values:
    sll.append(v)

# -------------------------------
# Test removeOptimal
# -------------------------------
print("\nTesting removeOptimal (remove 2nd from end):")
new_head = sll.removeOptimal(2)
print_list(new_head)
#~ TC: O(N-n)
#~ SC: O(1)