def spell_check():
    with open("dictionary.txt", "r") as file:
        words = file.readline()
    print(words)

spell_check()