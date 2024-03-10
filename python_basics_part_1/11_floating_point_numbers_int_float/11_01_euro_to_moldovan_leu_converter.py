# Euro to Moldovan Leu Converter
# This script converts a purchase cost in euros to Moldovan Leu using a fixed exchange rate.

# Constants for conversion rates
EURO_TO_DOLLAR_RATE = 1.09
DOLLAR_TO_MDL_RATE = 17.74

# Input for purchase cost in euros
purchase_cost_euros = float(input('Enter the purchase cost in euros: '))

# Conversion calculation
cost_in_mdl = purchase_cost_euros * EURO_TO_DOLLAR_RATE * DOLLAR_TO_MDL_RATE

# Print the converted cost
print('Purchase cost in MDL:', round(cost_in_mdl, 2))
