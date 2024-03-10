# New Apartment Evaluation
# This script evaluates if an apartment is suitable based on its price and size. 
# An apartment is suitable if the price is at most 10,000,000 and size is over 100 square meters,
# or if the price is at most 7,000,000 and size is over 80 square meters.

# Input for the apartment's price and size
apartment_price = int(input('Enter the apartment price: '))
apartment_size = int(input('Enter the number of square meters: '))

# Check if the apartment is suitable and print the result
if (apartment_price <= 10000000 and apartment_size > 100) or (apartment_price <= 7000000 and apartment_size > 80):
    print('The apartment is suitable.')
else:
    print('The apartment is not suitable.')
