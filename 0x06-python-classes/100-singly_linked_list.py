#!/usr/bin/python3
"""
    This is a module for a node and a singly linked list
    class
"""


class Node:
    """This is an empty class of a node

    Note:
    Args:
    Attributes:
    """
    def __init__(self, data=0, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not (isinstance(next_node, Node) or next_node == None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node


    @property
    def data(self):
        """ This property is a getter that return the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ This property is a setter of the property <size>"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @property
    def next_node(self):
        """ This property is a getter that return the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ This property is a setter of the property <size>"""
        if not isinstance(value, next_node):
            raise TypeError("next_node must be a Node object")
        else:
            self._next_node = value

    def my_print(self):
        """This property print a square with the character <#>"""
        if not self.__size:
            print("")

        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end="")
            print("")
