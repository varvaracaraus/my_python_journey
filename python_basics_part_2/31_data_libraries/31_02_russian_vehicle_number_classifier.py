import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car_pattern = r'\b[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}\b'
taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}[0-9]{3}[0-9]{2,3}\b'

private_cars = re.findall(private_car_pattern, text)
taxis = re.findall(taxi_pattern, text)

taxis = [taxi for taxi in taxis if taxi not in private_cars]

print("List of private car numbers:", private_cars)
print("List of taxi numbers:", taxis)
