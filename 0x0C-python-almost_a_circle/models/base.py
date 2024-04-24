#!/usr/bin/python3
"""
    This module contains the base class of the project and all its attributes
"""
import json


class Base:
    """
        That is the basic class that we create for out project.

    Attributes:
        __nb_objects (int): this is a private attributes about the number of
        object have been instanciated from the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            This method is the constructor of the base class
        Args:
            id (int): a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            This serialise a python object to a json object notation
        """
        data = ""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"

        data = json.dumps(list_dictionaries)

        return str(data)

    @classmethod
    def save_to_file(cls, list_objs):

        data = []
        filename = cls.__name__+'.json'

        with open(filename, 'w') as file:
            if list_objs is None:
                json.dump([], file)
            else:
                for i in list_objs:
                    data.append(i.to_dictionary())

                data = cls.to_json_string(data)
                file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
            This method deserialise a python to a string
        """
        data = ""

        if json_string == [] or json_string is None:
            return []

        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """
            This method creates an object from a dictionary
        """
#        print(f"DICT : {dictionary}")
        dummy = Rectangle(3, 5, 1)
#        print(dummy)
        dummy.update([1, 2, 3, 4], dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__+".json"

        with open(filename, "r+") as file:
            data = json.load(file)

            print(data)




class Rectangle(Base):
    """
        This class is the implementation of a rectangle
    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): the absisse of the rectangle
        y (int): the ordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Getter and setter for the attribute : width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.typevalidator("width", width)

        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

# Getter and setter for the attribute : height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.typevalidator("height", height)

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

# Getter and setter for the attribute : x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.typevalidator("x", x)

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

# Getter and setter for the attribute : y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.typevalidator("y", y)

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

# Validator method
    def typevalidator(self, attribute, value):
        """
            This function is a validator to ensure that we get the right
            type for the attributes of our object
        Args:
            attribute (string): the name of the attribute
            value (int): the value of the attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    def area(self):
        """
            This function computes the are of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            This function displays the rectangle on the stdout
        """
        for i in range(self.y):
            print()

        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
            This function updates the attributes of the instance
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args is not None and len(args) != 0 and kwargs is None:

            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                for i in attributes:
                    if i == attr:
                        setattr(self, i, value)

    def to_dictionary(self):
        """
            This functino returns a dictionnary of a class
        """
        class_dict = dict()
        attributes = ['x', 'y', 'id', 'height', 'width']
        values = [self.x, self.y, self.id, self.height, self.width]

        for attr, value in zip(attributes, values):
            class_dict[attr] = value

        return class_dict
