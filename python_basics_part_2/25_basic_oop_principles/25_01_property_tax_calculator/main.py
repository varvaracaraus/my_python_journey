from real_estate import Apartment, Car, CountryHouse


def main() -> None:
    money = float(input("Enter the amount of your money: "))
    property_type = input("Enter the type of property (Apartment, Car, CountryHouse): ")
    worth = float(input("Enter the value of the property: "))

    property_classes = {'Apartment': Apartment, 'Car': Car, 'CountryHouse': CountryHouse}
    property_class = property_classes.get(property_type)

    if property_class:
        ownership = property_class(worth)
        tax = ownership.tax()
        print(f"The tax on your property is: {tax:.2f}")
        if money < tax:
            print(f"You are short of {tax - money:.2f} to pay the tax")
        else:
            print("You have enough funds to pay the tax")
    else:
        print("Unknown property type")


main()
