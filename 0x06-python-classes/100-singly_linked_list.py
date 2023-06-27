#!/usr/bin/python3
"""This module defines a Node class and a Singly Linked list class"""

class Node:
    """This is a node object for a linked list"""
    def __init__(self, data, next_node=None):
        self.data(data)
        self.next_node(next_node)
        
    @property
    def data(self):
        """Getter for self.__data
        
        Returns:
            self.__data (int)
        """

    @data.setter
    def data(self, data):
        """Setter for self.__data
        
        Args:
            data (int): Data to be stored at this node
        
        Raises:
            TypeError: When data is not an int
        """
        if type(data) != int:
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
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        
class SinglyLinkedList:
    """A SinglyLinkedList that uses the Node class as a node"""
    def __init__(self):
        """Initializes the head to none"""
        self.__head == None

    def sorted_insert(self, value):
        """Inserts a node in the linked list at its correct sorted position
        in the linked list in ascending order
        
        Args:
            value (int): value to be inserted at the node

        Raises:
            TypeError: When value is not an int
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next_node is not None:
            if new_node.data > temp.data:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node

    def __repr__(self):
        """Returns a string representation of the LinkedList"""
        res = ''
        temp = self.head
        while temp.next_node is not None:
            res += f'{temp.data}\n'
        if temp is not None:
            res += f'{temp.data}'
        return res
