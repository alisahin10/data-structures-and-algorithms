class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty.")
            return
        iterator = self.head
        linkedListString = ''

        while iterator:
            linkedListString += str(iterator.data) + ' --> '
            iterator = iterator.next
        print(linkedListString)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == index -1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
            iterator = iterator.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        iterator = self.head
        while iterator:
            if iterator.data == data_after:
                iterator.next = Node(data_to_insert, iterator.next)
                break

            iterator = iterator.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        iterator = self.head
        while iterator.next:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next



if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_values(["Dog", "Cat", "Mouse", "Bird"])
    """
    linkedlist.insert_at_beginning(5)
    linkedlist.insert_at_beginning(89)
    linkedlist.insert_at_end(79)
    """
    linkedlist.print()
    print("Length of the Linked List:", linkedlist.get_length())
    linkedlist.remove_at(2)
    linkedlist.print()
    print("Length of the Linked List:", linkedlist.get_length())
    linkedlist.insert_at(0, "Camel")
    linkedlist.print()
    linkedlist.remove_by_value("Dog")
    linkedlist.remove_by_value("Cat")
    linkedlist.remove_by_value("Mouse")
    linkedlist.remove_by_value("Bird")
    linkedlist.remove_by_value("Camel")
    linkedlist.print()
