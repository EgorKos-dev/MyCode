def temperature_tracker():
    with open('hk-temperatures-2024.txt', 'r') as file:
        rounded_temp = round(float(temperatures.strip()))
        for temperatures in file:
            
temperature_tracker()