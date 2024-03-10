class Child:
    """
    Represents a child with a name, age, and mood states.

    Attributes:
        name (str): The name of the child.
        age (int): The age of the child.
        mood_hungry (str): The hunger mood of the child.
        mood_upset (str): The upset mood of the child.
    """

    def __init__(self, name: str, age: int, mood_hungry: str, mood_upset: str):
        """
        Initialize a new Child object.

        Args:
            name (str): The name of the child.
            age (int): The age of the child.
            mood_hungry (str): The initial hunger mood of the child.
            mood_upset (str): The initial upset mood of the child.
        """
        self.name = name
        self.age = age
        self.mood_hungry = mood_hungry
        self.mood_upset = mood_upset

    def feed(self) -> None:
        """
        Change the child's hunger mood to 'full'.
        """
        self.mood_hungry = "full"

    def comforted(self) -> None:
        """
        Change the child's upset mood to 'calm'.
        """
        self.mood_upset = "calm"

    def info(self) -> None:
        """
        Print the child's current state including name, age, and mood.
        """
        print(f"\n{self.name} is {self.age} years old, feeling {self.mood_hungry} and {self.mood_upset}.")
