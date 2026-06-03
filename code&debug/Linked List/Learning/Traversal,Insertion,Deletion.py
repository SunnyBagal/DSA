class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next

    def insertAtStart(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self,val):
        new_node = Node(val)
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def insertAtKth(self,val,position):
        new_node = Node(val)
        n = position - 1
        current = self.head
        for i in range(n):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def deleteFirstNode(self):
      if self.head is None:
          print("List is empty")
          return
      
      temp = self.head
      self.head = self.head.next
      temp.next = None

    def deleteAtEnd(self):
      if self.head is None:
          print("LL is empty")
          return

      if self.head.next is None:
          self.head = None
          return
   
      curr = self.head

      while curr.next.next is not None:
          curr = curr.next

      curr.next = None




a = Node(5)
b = Node(6)
c = Node(7)

a.next = b
b.next = c

ll = SinglyLinkedList()
ll.head = a

ll.insertAtStart(4)
ll.insertAtEnd(8)
ll.insertAtKth(1, 4)
ll.deleteFirstNode()
ll.deleteAtEnd()
ll.traversal()