def temperature_tracker():
    temperatures = open('hk-temperatures-2024.txt',):
    
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        
        print(f"Average Temperature: {avg_temp:.2f}")
        print(f"Maximum Temperature: {max_temp:.2f}")
        print(f"Minimum Temperature: {min_temp:.2f}")
    else:
        print("No temperatures were entered.")