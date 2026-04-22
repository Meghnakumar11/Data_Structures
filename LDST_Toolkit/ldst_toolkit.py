class DynamicArray:
    def __init__(self, arr, capacity=1):
        self.capacity = max(capacity, len(arr))
        self.arr = [None] * self.capacity
        self.size = len(arr)

        for i in range(self.size):
            self.arr[i] = arr[i]

    def append(self, x):
        if self.size == self.capacity:
            new_arr = [None] * (2 * self.capacity)
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            self.capacity *= 2
            print(f"Resized to capacity {self.capacity}")

        self.arr[self.size] = x
        self.size += 1
        

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.arr[self.size]

    def print_array(self):
        print("Array:", self.arr[:self.size])


# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = new_node

    def delete_by_value(self, x):
        if self.head is None:
            return

        if self.head.data == x:
            self.head = self.head.next
            return

        ptr = self.head
        prev = None

        while ptr and ptr.data != x:
            prev = ptr
            ptr = ptr.next

        if ptr is None:
            return

        prev.next = ptr.next

    def traverse(self):
        if self.head is None:
            print("List: []")
            return

        ptr = self.head
        arr = []
        while ptr:
            arr.append(ptr.data)
            ptr = ptr.next
        print("List:", arr)



# Doubly Linked List
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, x):
        new_node = DoubleNode(x)
        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after_node(self, target, x):
        ptr = self.head
        while ptr:
            if ptr.data == target:
                new_node = DoubleNode(x)
                new_node.prev = ptr
                new_node.next = ptr.next

                if ptr.next:
                    ptr.next.prev = new_node
                else:
                    self.tail = new_node

                ptr.next = new_node
                return
            ptr = ptr.next

    def delete_at_position(self, pos):
        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return

        ptr = self.head
        count = 0

        while ptr and count < pos:
            ptr = ptr.next
            count += 1

        if ptr is None:
            return

        if ptr.prev:
            ptr.prev.next = ptr.next
        if ptr.next:
            ptr.next.prev = ptr.prev
        else:
            self.tail = ptr.prev

    def traverse(self):
        if self.head is None:
            print("List: []")
            return

        ptr = self.head
        arr = []
        while ptr:
            arr.append(ptr.data)
            ptr = ptr.next
        print("List:", arr)



# Stack using SLL
class Stack:
    def __init__(self):
        self.stackLL = SinglyLinkedList()
        self.size = 0

    def push(self, x):
        self.stackLL.insert_at_start(x)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        val = self.stackLL.head.data
        self.stackLL.head = self.stackLL.head.next
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0:
            return None
        return self.stackLL.head.data


# Queue using SLL Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None

        val = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1
        return val

    def front(self):
        if self.head is None:
            return None
        return self.head.data



# Balanced Parentheses
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.size == 0:
                return False
            top = stack.peek()
            if top == pairs[char]:
                stack.pop()
            else:
                return False

    return stack.size == 0



# MAIN TEST CASES
if __name__ == "__main__":

    print("=== Dynamic Array ===")
    da = DynamicArray([], capacity=2)
    for i in range(10):
        da.append(i)
    da.print_array()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.print_array()

    print("\n=== Singly Linked List ===")
    sll = SinglyLinkedList()
    sll.insert_at_start(10)
    sll.insert_at_start(20)
    sll.insert_at_start(30)
    sll.traverse()

    sll.insert_at_end(40)
    sll.insert_at_end(50)
    sll.insert_at_end(60)
    sll.traverse()

    sll.delete_by_value(20)
    sll.traverse()

    print("\n=== Doubly Linked List ===")
    dll = DoublyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        dll.insert_at_end(val)
    dll.traverse()

    dll.insert_after_node(20, 25)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    print("\n=== Stack ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())

    print("\n=== Queue ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front())

    print("\n=== Balanced Parentheses ===")
    test_exprs = ["([])", "([)]", "(((", ""]
    for expr in test_exprs:
        print(expr, "->", is_balanced(expr))
