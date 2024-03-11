from functools import reduce
from typing import List

FloatList = List[float]
StringList = List[str]
IntList = List[int]

cube_and_round = lambda number: round(number ** 3, 3)

is_name_long_enough = lambda name: len(name) >= 5

product_of_numbers = lambda numbers: reduce(lambda x, y: x * y, numbers)
