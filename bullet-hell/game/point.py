class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance. 
        _y (Point): The vertical distance.
    """
    
    def __init__(self, x, y):
        """The class constructor.
        
        Args:
            self (Point): An instance of Point.
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            self (Point): An instance of Point.
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.

        """
        return Point(self._x * factor, self._y * factor)

    def reverse(self):
        """Gets a new Point that is the reverse of this one.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            Point: A new Point that is reversed.
        """
        return self.scale(-1)

    def is_zero(self):
        """
        Returns True if both the x and y coordinate are 0.
        """
        return self._x == 0 and self._y == 0