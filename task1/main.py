class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list_head = None
        current = self.head

        while current:
            next_node = current.next
            if sorted_list_head is None or current.data < sorted_list_head.data:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_node = sorted_list_head
                while search_node.next and current.data > search_node.next.data:
                    search_node = search_node.next
                current.next = search_node.next
                search_node.next = current
            current = next_node
        self.head = sorted_list_head


def merge_sorted_lists(l1, l2):
    merged_list = LinkedList()
    dummy_node = Node()
    tail = dummy_node

    c1 = l1.head
    c2 = l2.head

    while c1 and c2:
        if c1.data <= c2.data:
            tail.next = c1
            c1 = c1.next
        else:
            tail.next = c2
            c2 = c2.next
        tail = tail.next

    if c1:
        tail.next = c1
    elif c2:
        tail.next = c2

    merged_list.head = dummy_node.next
    return merged_list


llist = LinkedList()

llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

llist.insert_at_end(20)
llist.insert_at_end(25)
llist.insert_at_end(7)

print("Оригінальний зв'язний список:")
llist.print_list()

llist.reverse()
print("\nЗв'язний список після реверсування:")
llist.print_list()

llist.insertion_sort()
print("\nЗв'язний список після сортування вставками:")
llist.print_list()

list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

print("\nПерший відсортований список:")
list1.print_list()
print("Другий відсортований список:")
list2.print_list()

merged_list = merge_sorted_lists(list1, list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()
