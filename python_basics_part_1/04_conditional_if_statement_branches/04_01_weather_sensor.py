# Weather Sensor
# This script asks the user about the weather condition and provides a suggestion based on the input.

# Input for weather condition
# 1 for rain, 0 for no rain
weather_condition = int(input("What's the weather like outside? (Enter 1 for rain, 0 for no rain): "))

# Provide suggestion based on weather condition
if weather_condition == 1:
    print("It's raining. Take an umbrella!")

if weather_condition == 0:
    print('There is no rain!')
