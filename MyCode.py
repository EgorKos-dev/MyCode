# Define a function to read names from a file and generate initial passwords
def listnames():
    names = []
    try:
        with open("Names.txt", "r") as file:
            try:
                # Read names from file and store them in a list
                for line in file:
                    names.append(line.strip())
            # Add exception handling for invalid entries
            except ValueError:
                print("Warning: Skipping invalid entry (not a string).")
            # Generate and print initial passwords for each name
            for name in names:
                # Extract parts
                first_part = name[0:3]
                second_part = name[-3:]
                # Print the generated password
                print(f"The intital password for {name} is: {first_part.lower()}{second_part}@567")
    # Add exception handling for file not found    
    except FileNotFoundError:
        print("Error: File 'Names.txt' not found.")
    return names
# Run the list names function
listnames()