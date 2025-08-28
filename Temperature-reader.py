import time

def temperature_tracker():
    global tot_temp
    global avg_temp
    global max_temp
    global min_temp
    templist = []
    roundlist = []
    
    with open('hk-temperatures-2024.txt', 'r') as file:
        readtemp = file.readlines()
        for line in readtemp:
            Temp = float(line.strip())
            templist.append(Temp)
        for Temp in templist:
            roundtemp = round(Temp)
            roundlist.append(roundtemp)
    
    tot_temp = sum(roundlist)
    avg_temp = tot_temp / len(roundlist)
    max_temp = max(roundlist)
    min_temp = min(roundlist)

tot_temp = 0
avg_temp = 0
max_temp = -100
min_temp = 100

while True:
    temperature_tracker()
    print(f"The total temperature is: {tot_temp}")
    print(f"The average temperature is: {avg_temp}")
    print(f"The maximum temperature is: {max_temp}")
    print(f"The minimum temperature is: {min_temp}")
    time.sleep(86400)