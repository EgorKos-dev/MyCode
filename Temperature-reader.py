def temperature_tracker():
    with open('hk-temperatures-2024.txt', 'r') as file:
        readtemp = file.readlines()
        for readtemp in file:
            Temp = float(readtemp.strip())
            templist.append(Temp)
        for Temp in templist:
            roundtemp = round(Temp)
            roundlist.append(roundtemp)

            
templist = []
roundlist = []
tot_temp = 0
Temp = 0
max_temp = -100
min_temp = 100
temperature_tracker()
print (roundlist)