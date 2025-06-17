import random

def play_hangman():                          # Start the game
    # Unique word categories
    categories = {
        "Fruits": ["apple", "banana", "grape", "mango", "peach"],
        "Animals": ["tiger", "zebra", "panda", "lion", "koala"],
        "Colors": ["green", "white", "black", "blue", "purple"]
    }
    
    # Select a random category and word
    category = random.choice(list(categories.keys()))
    secret_word = random.choice(categories[category])
    
    # Game setup
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6
    display_word = ['_'] * len(secret_word)
    
    # Game introduction
    print(f"\nWelcome to Unique Hangman! Category: {category.upper()}")
    print(f"Guess this {len(secret_word)}-letter word:")
    print(" ".join(display_word))
    
    while wrong_guesses < max_wrong and '_' in display_word:
        # Get and validate guess
        while True:
            guess = input("\nEnter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already tried that letter!")
                else:
                    break
            else:
                print("Please enter a single letter (a-z).")
        
        guessed_letters.add(guess)
        
        # Check guess
        if guess in secret_word:
            print("Good guess!")
            # Update display word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"Oops! Wrong guess. {max_wrong - wrong_guesses} attempts left.")
        
        # Display current status
        print("\n" + " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    # Game conclusion
    if '_' not in display_word:
        print(f"\nCongratulations! You guessed '{secret_word}' correctly!")
    else:
        print(f"\nGame over! The word was '{secret_word}'")

# Start the game
play_hangman()