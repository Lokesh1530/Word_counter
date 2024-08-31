def word_count(sentence):
    # whitespaces at the beginning and at the end are removed
    sentence = sentence.strip()
    # Checks if the text is empty or not
    if not sentence:
        return 0
    # Split the text by spaces to count words
    words = sentence.split()
    return len(words)

def main():
    # Taking input from the user
    sentence = input("\nPlease type here: ")
    # Calling the word_count function
    count = word_count(sentence)
    # Displaying the result
    if count == 0:
        print("You have entered an empty text or only spaces.\n")
    else:
        print(f"The number of words in the given text is: {count}\n")

if __name__ == "__main__":
    main()

