from utils import FloatList, StringList, IntList, cube_and_round, is_name_long_enough, product_of_numbers

if __name__ == "__main__":
    floats: FloatList = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: StringList = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: IntList = [22, 33, 10, 6894, 11, 2, 1]

    cubed_floats = list(map(cube_and_round, floats))
    filtered_names = list(filter(is_name_long_enough, names))
    numbers_product = product_of_numbers(numbers)

    print("Cubed Floats:", cubed_floats)
    print("Filtered Names:", filtered_names)
    print("Product of Numbers:", numbers_product)
