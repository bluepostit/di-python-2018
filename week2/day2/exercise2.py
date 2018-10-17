class Square:
    """Simple class representing a square shape.

    Note that this class does NOT have an __init__ function!
    Instead, any code that uses this class needs to set the 'length'
    attribute on any Square objects that it creates.

    eg. s = Square()
        s.length = 100
        area = s.get_area() --> area will be 10000

    An alternative would be to define an __init__ function, like this:
    def __init__(self, length):
        self.length = length

    Then, you could simply do the above code in a shorter form:
    eg. s = Square(100)
        area = s.get_area() --> area will be 10000

    Neither way is wrong - but this exercise asked for the first way.
    """
    def get_area(self):
        return self.length ** 2

    def get_perimeter(self):
        """Get the perimeter: length * 4"""
        return self.length * 4


def main():
    little = Square()
    little.length = 3
    big = Square()
    big.length = 104.5

    print("Square 'little' - length: {}; area: {}; perimeter: {}"
          .format(little.length, little.get_area(), little.get_perimeter()))
    print("Square 'big' - length: {}; area: {}; perimeter: {}"
          .format(big.length, big.get_area(), big.get_perimeter()))


############ BONUS ############
def show_square_info(square):
    """Takes a single Square object as an argument.
    Shows information about the Square object by accessing
    its attributes."""
    print("Square info: length: {}; area: {}; perimeter: {}"
          .format(square.length, square.get_area(), square.get_perimeter()))


def main_with_bonus():
    little = Square()
    little.length = 3
    big = Square()
    big.length = 104.5

    print("For square 'little':")
    show_square_info(little)
    print("For square 'big':")
    show_square_info(big)

##############################


# Uncomment one (or both) to see results:
# main()
# main_with_bonus()
