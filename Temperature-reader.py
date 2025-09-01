# Import necessary library (time)
import time
# Define function to read temperatures from file and calculate statistics
def temperature_tracker():
    # Declare global variables, so they can be modified inside the function
    global tot_temp
    global avg_temp
    global max_temp
    global min_temp
    # Initialize temporary lists to store raw and rounded temperatures
    templist = []
    roundlist = []
    # Try to read temperatures from file and process them through temporary list into rounded list
    try:
        with open('hk-temperatures-2024.txt', 'r') as file:
            readtemp = file.readlines()
            for line in readtemp:
                try:
                    Temp = float(line.strip())
                    templist.append(Temp)
                # Add exception handling for invalid entries
                except ValueError:
                    print(f"Warning: Skipping invalid entry '{line.strip()}' (not a number).")
            for Temp in templist:
                roundtemp = round(Temp)
                roundlist.append(roundtemp)
        # Calculate total, average, maximum, and minimum temperatures
        if roundlist:
            tot_temp = sum(roundlist)
            avg_temp = tot_temp / len(roundlist)
            max_temp = max(roundlist)
            min_temp = min(roundlist)
    #Add exception handling for file not found
    except FileNotFoundError:
        print("Error: File 'hk-temperatures-2024.txt' not found.")
        tot_temp = 0
        avg_temp = 0
        max_temp = 0
        min_temp = 0
# Initialize global variables
tot_temp = 0
avg_temp = 0
max_temp = 0
min_temp = 0
# Run the temperature tracker function every 24 hours (86400 seconds)
while True:
    temperature_tracker()
    print(f"The total temperature is: {tot_temp}")
    print(f"The average temperature is: {avg_temp}")
    print(f"The maximum temperature is: {max_temp}")
    print(f"The minimum temperature is: {min_temp}")
    time.sleep(86400)