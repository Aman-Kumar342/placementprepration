import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def create_loop(self, position):
        if position == -1 or not self.head:
            return
        temp = self.head
        loop_node = None
        count = 1
        while temp.next:
            if count == position:
                loop_node = temp
            temp = temp.next
            count += 1
        temp.next = loop_node

    def detect_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    ll = LinkedList()
    for _ in range(n):
        ll.add_node(int(next(it)))
    position = int(next(it, -1))
    ll.create_loop(position)
    if ll.detect_loop():
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")


if __name__ == "__main__":
    main()
