class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class thor:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
            self.tail.next = node.next
        else:
            self.tail.next = node
            self.tail = node

    def remove_num(self, val):
        if self.find_node(val):
            pass

        else:
            print("Given number is not in the list")

    def find_node(self, val):
        print(val)
        node = self.head
        while node:
            print(node.value, val, node.value == val)
            if (node.value == val):
                return 1
            node = node.next
        return 0

    def is_empty(self):
        if not self.head:
            return 0
        else:
            return 1
        
    def show_list(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next
        print()

    def get_head(self):
        return self.head.value
    
    def get_tail(self):
        return self.tail.value

var = thor()
list = [12, 51, 2, 16, 5]

for i in list:
    var.add(i)

var.show_list()



















