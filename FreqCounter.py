#Create a function to count the frequency of words in a text file
def word_frequency():
    #Declare a dictionary to store word counts
    word_count = {}
    #Open the text file and read its contents and remove any extra punctuation
    with open("frequency-counter.txt", "r") as file:
        text = file.read()
        for word in text.split():
            word = word.strip().lower().strip('.,!?;"()[]{}')
            #Add words to the dictionary and count their occurrences, then print the results in descending order
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")

#Run the word frequency function
word_frequency()