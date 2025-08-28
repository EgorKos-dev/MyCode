#Define a function to check for misspelled words
def spell_check():
    #Declare global variable to count misspelled words
    global misspelled
    correct_words = []
    mystery_words = []
    #Call out to a dictionary file and a mystery text file
    #Read the files and store the words in two separate lists
    with open("dictionary.txt", "r") as file:
        text = file.readlines()
        for word in text:
            correct_words.append(word.strip().lower())
    with open("mystery-text.txt", "r") as file:
        text = file.read()
        for word in text.split():
            mystery_words.append(word.strip().lower())
    #Compare the two lists and count how many words are misspelled in integers
    for word in mystery_words:
        if word not in correct_words:
            misspelled += 1

#Initialize global variable
misspelled = 0
#Run the spell check function and print the number of misspelled words
spell_check()
print(f"The number of misspelled words is: {misspelled}")