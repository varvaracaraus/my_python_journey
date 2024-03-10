from typing import Optional


class Element:
    """
    Represents a basic elemental entity.
    """

    def __init__(self, name: str):
        """
        Initialize the element with a name.
        Args:
            name (str): Name of the element.
        """
        self.name = name

    def __add__(self, other: 'Element') -> Optional['Element']:
        """
        Defines the addition behavior for combining two elements.
        By default, returns None, indicating no specific combination.
        Args:
            other (Element): Another element to combine with.
        Returns:
            Optional[Element]: Resulting element or None.
        """
        return None


class Water(Element):
    def __init__(self):
        super().__init__('Water')

    def __add__(self, other: 'Element') -> Optional['Element']:
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Earth):
            return Mud()
        elif isinstance(other, Fire):
            return Steam()
        else:
            return None


class Air(Element):
    def __init__(self):
        super().__init__('Air')

    def __add__(self, other: 'Element') -> Optional['Element']:
        if isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
        else:
            return None


class Fire(Element):
    def __init__(self):
        super().__init__('Fire')

    def __add__(self, other: 'Element') -> Optional['Element']:
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None


class Earth(Element):
    def __init__(self):
        super().__init__('Earth')

    def __add__(self, other: 'Element') -> Optional['Element']:
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Mud()
        else:
            return None


class Storm(Element):
    def __init__(self):
        super().__init__('Storm')


class Steam(Element):
    def __init__(self):
        super().__init__('Steam')


class Mud(Element):
    def __init__(self):
        super().__init__('Mud')


class Lightning(Element):
    def __init__(self):
        super().__init__('Lightning')


class Dust(Element):
    def __init__(self):
        super().__init__('Dust')


class Lava(Element):
    def __init__(self):
        super().__init__('Lava')
