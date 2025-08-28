def spell_check():
    global misspelled
    correct_words = []
    mystery_words = []
    with open("dictionary.txt", "r") as file:
        text = file.readlines()
        for word in text:
            correct_words.append(word.strip().lower())
    with open("mystery-text.txt", "r") as file:
        text = file.read()
        for word in text.split():
            mystery_words.append(word.strip().lower())
    for word in mystery_words:
        if word not in correct_words:
            misspelled = misspelled + 1


misspelled = 0
spell_check()
print(f"The number of misspelled words is: {misspelled}")