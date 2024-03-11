from date_class import Date

# Demonstrate the use of the Date class
date = Date.from_string('29-02-2024')
print(date)
print(Date.is_date_valid('31-13--2077'))
print(Date.is_date_valid('31-13-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('13-12-1991'))
