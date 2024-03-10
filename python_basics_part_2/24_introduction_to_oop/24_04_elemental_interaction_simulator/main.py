from elements import Element, Water, Air, Fire, Earth


def combine_and_print(element1: Element, element2: Element) -> None:
    """
    Combine two elements and print the name of the resulting element,
    or a message if there's no combination.
    Args:
        element1 (Element): The first element to combine.
        element2 (Element): The second element to combine.
    Returns:
        None
    """
    result = element1 + element2
    if result is not None:
        print(result.name)
    else:
        print("No combination")


# Instance creation and combination demonstration code
water_element = Water()
air_element = Air()
fire_element = Fire()
earth_element = Earth()

# Demonstrating the specified element combinations
combine_and_print(water_element, air_element)  # Water + Air = Storm
combine_and_print(water_element, fire_element)  # Water + Fire = Steam
combine_and_print(water_element, earth_element)  # Water + Earth = Mud
combine_and_print(air_element, fire_element)  # Air + Fire = Lightning
combine_and_print(air_element, earth_element)  # Air + Earth = Dust
combine_and_print(fire_element, earth_element)  # Fire + Earth = Lava
