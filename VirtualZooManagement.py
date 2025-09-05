# Import necessary modules
import random
# Define the function to ask the user to add a new animal to the zoo
def virtual_zoo_management():
    global counter
    animalname = []
    animalspecies = []
    animalage = []
    animalweight = []
    print("Welcome to the Virtual Zoo Management System!")
    for i in range(counter):
        new_animal = input("Enter the name of the animal, species, age and weight you want to add (or type 'exit' to quit): ")
        if new_animal.lower() == 'exit':
            print("Exiting the Virtual Zoo Management System. Goodbye!")
            break
        elif new_animal:
            for i in range(4):
                if i == 0:
                    animalname = new_animal.split()[0]
                elif i == 1:
                    animalspecies = new_animal.split()[1]
                elif i == 2:
                    if int(new_animal.split()[2]) < 0 or int(new_animal.split()[2]) > 50:
                        print("Error: Age must be in range of 1-50. Please re-enter the details.")
                        return virtual_zoo_management()
                    animalage = new_animal.split()[2]
                elif i == 3:
                        if int(new_animal.split()[3]) < 0 or int(new_animal.split()[3]) > 1000:
                            print("Error: Weight must be in range of 0.1-1000. Please re-enter the details.")
                            return virtual_zoo_management()
                        animalweight = new_animal.split()[3]
            print(f"Animal added: Name: {animalname}, Species: {animalspecies}, Age: {animalage}, Weight: {animalweight}kg. Is that correct?")
            confirmation = input("Type 'yes' to confirm or 'no' to re-enter the details: ")
            if confirmation.lower() == 'yes':
                print(f"Successfully added {animalname} the {animalspecies} to the zoo!")
            else:
                virtual_zoo_management()   
        counter -= 1

counter = 10
zoo_management = input("1. Add a new animal to the zoo\n2. View all the animals\n3. Zoo summary\nChoose an option (1-3): ")
if add_animal.lower() == 'yes':
    virtual_zoo_management()