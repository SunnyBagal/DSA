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

  def delete_All_Occurance(self, k):
    temp = self.head
    while temp is not None:
        if temp.val == k:
            next_node = temp.next  # save next
            # Case 1: deleting head
            if temp.prev is None:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
            # Case 2: deleting middle or tail
            else:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
            temp = next_node  
        else:
            temp = temp.next

    #~ TC: O(N)
    #~ SC: O(1)

dll = DoublyLinkedList()
nums = [5,2,3,2,10]
for i in range(len(nums)-1,-1,-1):
  dll.insert_at_head(nums[i])
dll.traverse_forward()

dll.delete_All_Occurance(2)

dll.traverse_forward()