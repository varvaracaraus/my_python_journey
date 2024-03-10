from child import Child


class Parent:
    """
    Represents a parent with a name, age, and a list of children.

    Attributes:
        name (str): The name of the parent.
        age (int): The age of the parent.
        children (list of Child): The children of the parent.
    """

    def __init__(self, name: str, age: int):
        """
        Initialize a new Parent object.

        Args:
            name (str): The name of the parent.
            age (int): The age of the parent.
        """
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child: 'Child') -> None:
        """
        Add a child to the parent's list of children if the age difference is appropriate.

        Args:
            child (Child): The child to be added.
        """
        if self.age - child.age > 16:
            self.children.append(child)
            print(f"{child.name} is added to the family.")
        else:
            print(f"{child.name} is not added to the family because of the age difference.")

    def feed_child(self, child: 'Child') -> None:
        """
        Simulate feeding a child.

        Args:
            child (Child): The child to be fed.
        """
        print(f"\n{self.name} feeds {child.name}!")
        child.feed()

    def comfort_child(self, child: 'Child') -> None:
        """
        Comfort a child.

        Args:
            child (Child): The child to be comforted.
        """
        print(f"\n{self.name} comforts {child.name}!")
        child.comforted()
