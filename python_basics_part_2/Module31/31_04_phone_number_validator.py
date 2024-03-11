import re
from typing import List


def validate_phone_numbers(phone_numbers: List[str]) -> List[str]:
    """
    Validates a list of phone numbers against specific criteria.

    Parameters:
    phone_numbers (List[str]): A list of phone numbers to be validated.

    Returns:
    List[str]: Messages indicating whether each phone number meets the criteria.
    """
    pattern = re.compile(r'^[89]\d{9}$')
    results = []

    for i, number in enumerate(phone_numbers, 1):
        if pattern.match(number):
            results.append(f"number {i}: all good")
        else:
            results.append(f"number {i}: not valid")

    return results


if __name__ == "__main__":
    phone_number = ['9999999999', '999999-999', '99999x9999']
    result = validate_phone_numbers(phone_number)
    for r in result:
        print(r)
