#!/usr/bin/python3
"""This module defines a Node class and a Singly Linked list class"""


class Node:
    """This is a node object for a linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for self.__data

        Returns:
            self.__data (int)
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Setter for self.__data

        Args:
            data (int): Data to be stored at this node

        Raises:
            TypeError: When data is not an int
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """Getter for next_node

        Returns:
            self.__next_node (Node)
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """Setter for next_node

        Args:
            next_node (Node, None): Next node in the linked list

        Raises:
            TypeError: When next_node is not None and is not a Node object
        """
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """A SinglyLinkedList that uses the Node class as a node"""
    def __init__(self):
        """Initializes the head to none"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node in the linked list at its correct sorted position
        in the linked list in ascending order

        Args:
            value (int): value to be inserted at the node

        Raises:
            TypeError: When value is not an int
        """
        new_node = Node(value)
        temp = self.__head
        prev = None
        while temp is not None and new_node.data > temp.data:
            prev = temp
            temp = temp.next_node
        if prev is None:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        prev.next_node = new_node
        new_node.next_node = temp

    def __repr__(self):
        """Returns a string representation of the LinkedList"""
        res = ''
        temp = self.__head
        if temp is None:
            return res
        while temp.next_node is not None:
            res += f'{temp.data}\n'
            temp = temp.next_node
        if temp is not None:
            res += f'{temp.data}'
        return res
