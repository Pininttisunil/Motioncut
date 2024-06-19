def count_words(text):
    # Split the text by whitespace and filter out any empty strings
    words = text.split()
    # Return the length of the list which is the word count
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    # Error handling: Check if the input is empty
    if not user_input.strip():
        print("Error: The input is empty. Please enter some text.")
    else:
        # Call the count_words function and store the result
        word_count = count_words(user_input)
        # Display the word count
        print(f"The number of words in the entered text is: {word_count}")

if __name__ == "__main__":
    main()

