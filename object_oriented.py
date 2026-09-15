# object_oriented.py
"""Python Essentials: Object Oriented Programming.
<Name>
<Class>
<Date>
"""


class Backpack:
    """Represent a backpack with an owner, color, capacity, and contents.

    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the color of the backpack.
        max_size (int): the maximum number of items the backpack can hold.
        contents (list): the contents of the backpack.
    """

    def __init__(self, name, color, max_size=5):
        """Initialize an empty backpack with its identifying information.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int): the maximum number of items the backpack can hold;
                defaults to 5.
        """
        self.name = name
        self.color = color # TASK 13
        self.max_size = max_size # TASK 13
        self.contents = []

    def put(self, item):
        """Add an item unless the backpack has reached its maximum capacity.

        Parameters:
            item: the item to add to the backpack.

        Prints:
            "No Room!" when the backpack is already full.
        """
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def dump(self): # TASK 13
        """Remove all items from the backpack and leave it empty."""
        self.contents = []

    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)

    # Magic Methods -----------------------------------------------------------

    def __eq__(self, other):  # Task 15
        """Return True when two backpacks match in name, color, and size."""
        if not isinstance(other, Backpack):
            return NotImplemented
        return (self.name == other.name
                and self.color == other.color
                and len(self.contents) == len(other.contents))

    def __str__(self):  # Task 15
        """Return a formatted description of the backpack."""
        return (f"Owner:\t\t{self.name}\n"
                f"Color:\t\t{self.color}\n"
                f"Size:\t\t{len(self.contents)}\n"
                f"Max Size:\t{self.max_size}\n"
                f"Contents:\t{self.contents}")

    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)


def test_backpack():
    """Check Backpack attributes, capacity handling, and dumping contents."""
    backpack = Backpack("Alex", "blue", max_size=2)
    assert backpack.name == "Alex"
    assert backpack.color == "blue"
    assert backpack.max_size == 2
    assert backpack.contents == []

    backpack.put("book")
    backpack.put("pen")
    backpack.put("laptop")
    assert backpack.contents == ["book", "pen"]

    backpack.dump()
    assert backpack.contents == []


# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


class Jetpack(Backpack):
    """Represent a backpack with a limited fuel supply for flying.

    A Jetpack has all of the identifying information, capacity, contents, and
    item-management behavior of a Backpack. It also tracks fuel, which can be
    consumed with fly() and completely emptied with dump().

    Attributes:
        name (str): the name of the jetpack's owner.
        color (str): the color of the jetpack.
        max_size (int): the maximum number of items the jetpack can hold.
        contents (list): the items currently stored in the jetpack.
        fuel (int or float): the amount of fuel remaining in the jetpack.
    """

    def __init__(self, name, color, max_size=2, fuel=10):
        """Initialize a jetpack with a capacity and fuel supply.

        Parameters:
            name (str): the name of the jetpack's owner.
            color (str): the color of the jetpack.
            max_size (int): the maximum number of items it can hold;
                defaults to 2.
            fuel (int or float): the initial amount of fuel;
                defaults to 10.
        """
        super().__init__(name, color, max_size)
        self.fuel = fuel

    def fly(self, fuel_burned):
        """Burn fuel to fly if enough fuel remains.

        Parameters:
            fuel_burned (int or float): the amount of fuel to consume.

        Prints:
            "Not enough fuel!" if fuel_burned exceeds the remaining fuel.
            In that case, the fuel amount is left unchanged.
        """
        if fuel_burned > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= fuel_burned

    def dump(self):
        """Empty the jetpack's contents and set its fuel to zero."""
        super().dump()
        self.fuel = 0


class ContentFilter:
    """Read and store the contents of a valid text file.

    Attributes:
        filename (str): the name of the file that was successfully opened.
        contents (str): the complete contents of the file as one string.
    """

    def __init__(self, filename):
        """Open a valid file and store its name and complete contents.

        If filename is not a valid file name or cannot be opened, repeatedly
        prompt the user for another filename until a file is successfully read.

        Parameters:
            filename (str): the initial file name to try.
        """
        while True:
            try:
                with open(filename, "r") as input_file:
                    self.contents = input_file.read()
                self.filename = filename
                break
            except (FileNotFoundError, TypeError, OSError):
                filename = input("Please enter a valid file name: ")

