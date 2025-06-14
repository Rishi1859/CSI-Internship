class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def add(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        current=self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current=current.next
    
    def delete_nth(self,n):
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        if n == 1:
            self.head=self.head.next
            return
        
        current=self.head
        for i in range(n-2):
            if not current.next:
                raise IndexError(f"Index {n} out of range")
            current=current.next
        
        if not current.next:
            raise IndexError(f"Index {n} out of range")
        current.next=current.next.next

ll=LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.add(i)
print("Original list:")
ll.print_list()
ll.delete_nth(3)
print("After deleting 3rd element:")
ll.print_list()
try:
    ll.delete_nth(10)
except IndexError as e:
    print(f"Error:{e}")
try:
    empty_list =LinkedList()
    empty_list.delete_nth(1)
except IndexError as e:
    print(f"Error:{e}")