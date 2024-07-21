import random

# Word categories and words
categories = {
    "animals": ["lion", "tiger", "bear", "zebra", "giraffe"],
    "countries": ["france", "germany", "italy", "spain", "portugal"],
    "movies": ["avatar", "inception", "interstellar", "thor", "hulk"]
}

# Game settings
max_guesses = 6
difficulty_levels = {
    "easy": (6, 5),  # (max_guesses, word_length)
    "medium": (5, 6),
    "hard": (4, 7)
}

def get_word(category):
    return random.choice(categories[category])

def draw_hangman(guesses):
    stages = [
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |      
        -
        """,
        """
        --------
        |      |
        |      O
        |      
        |      |
        |      
        -
        """,
        """
        --------
        |      |
        |      
        |     
        |      
        |      
        -
        """,
        """
        --------
        |      
        |     
        |     
        |      
        |      
        -
        """
    ]
    return stages[guesses]

def play_hangman():
    category = input("Choose a category: ")
    word = get_word(category)
    word_length = len(word)
    guesses = 0
    guessed_letters = []
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    max_guesses, word_length = difficulty_levels[difficulty]

    print(f"Word has {word_length} letters.")

    while guesses < max_guesses:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please guess a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            guesses += 1
            print(f"Incorrect! {max_guesses - guesses} guesses left.")
            print(draw_hangman(guesses))
        else:
            print("Correct!")

        # Check if the word has been completely guessed
        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you won!")
            return

    print(f"Game over! The word was {word}.")

play_hangman()
