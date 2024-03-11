from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

results = list(map(lambda i: (letters[i], numbers[i]), range(min(len(letters), len(numbers)))))
print(results)
