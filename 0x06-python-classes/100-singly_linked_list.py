#!/usr/bin/python3
class Node:
    """
    Class to define a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a Node object with data and next_node.

        Args:
            data (int): Data to be stored in the node.
            next_node (Node, optional): Next node in the linked list.
        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            int: Data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): Data to be set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        Returns:
            Node: Next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): Next node to be set.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self._next_node = value


class SinglyLinkedList:
    """
    Class to define a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty SinglyLinkedList object.
        """
        self._head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list

        Args:
            value (int): Value of the new Node to be inserted.
        """
        new_node = Node(value)
        if self._head is None or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Convert the SinglyLinkedList object to a string representation.

        Returns:
            str: String representation of the linked list.
        """
        current = self._head
        list_str = ""
        while current is not None:
            list_str += str(current.data) + "\n"
            current = current.next_node
        return list_str.rstrip()
