
import random
counter = 10

def menu():
    animal_options = input("1. Add a new animal to the zoo\n2. View all the animals\n3. Zoo summary\nChoose an option (1-3): ")
    if animal_options.lower() == '1':
        add_animalfunc()

def add_animalfunc():
    global counter
    print("Welcome to the Virtual Zoo Management System!")
    while counter > 0:
        new_animal = input("Enter the name of the animal, species, age and weight you want to add (or type 'exit' to quit): ")
        if new_animal.lower() == 'exit':
            print("Exiting the System. Goodbye!")
            menu()
            break
        elif new_animal:
            parts = new_animal.split()
            if len(parts) != 4:
                print("Error: Please enter exactly 4 values (name, species, age, weight).")
                continue
            animalname, animalspecies, animalage, animalweight = parts
            try:
                age = int(animalage)
                weight = float(animalweight)
            except ValueError:
                print("Error: Age must be an integer and weight must be a real number.")
                continue
            if age < 1 or age > 50:
                print("Error: Age must be in range of 1-50. Please re-enter the details.")
                continue
            if weight < 0.1 or weight > 1000:
                print("Error: Weight must be in range of 0.1-1000. Please re-enter the details.")
                continue
            print(f"Animal added: Name: {animalname}, Species: {animalspecies}, Age: {age}, Weight: {weight}kg. Is that correct?")
            confirmation = input("Type 'yes' to confirm or 'no' to re-enter the details: ")
            if confirmation.lower() == 'yes':
                with open("Animals.txt", "a") as add_animal:
                    add_animal.write(f"{[animalname, animalspecies, age, weight]}\n")
                print(f"Successfully added {animalname} the {animalspecies} to the zoo!")
                counter -= 1
            else:
                continue
    if counter == 0:
        print("You have reached the maximum number of animals you can add.")
        menu()

menu()