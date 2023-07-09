#!/usr/bin/python3
class Node:
    """
    Node class represents a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node with the given data and next_node.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list (default: None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value: The new value to set as the data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value: The next node to set.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new Node with the given value into the correct sorted position

        Args:
            value: The value to be inserted into the list.
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        if self.__head is None:
            return ""

        current_node = self.__head
        result = str(current_node.data) + "\n"

        while current_node.next_node is not None:
            current_node = current_node.next_node
            result += str(current_node.data) + "\n"

        return result.strip()
