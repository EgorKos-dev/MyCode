def temperature_tracker():
    temperatures = with open('hk-temperatures-2024.txt',) file:
    while True:
        temp_input = input("Enter temperature (or 'done' to finish): ")
        if temp_input.lower() == 'done':
            break
        try:
            temperature = float(temp_input)
            temperatures.append(temperature)
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'done'.")
    
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        
        print(f"Average Temperature: {avg_temp:.2f}")
        print(f"Maximum Temperature: {max_temp:.2f}")
        print(f"Minimum Temperature: {min_temp:.2f}")
    else:
        print("No temperatures were entered.")