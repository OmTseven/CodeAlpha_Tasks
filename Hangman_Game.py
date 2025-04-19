import random


words = ["python", "hangman", "programming", "computer", "keyboard", "monitor", "laptop", "desktop", "software", "hardware"]

hangman_stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

def hangman():
    print("\nWelcome to Hangman!")
    print("A classic game where you guess the word by suggesting letters.")
    print("You have 6 attempts to guess incorrectly. Good luck!")
    
    word = random.choice(words)
    display = ["_"] * len(word)
    guessed = set()
    remaining_guesses = 6
    
    while "_" in display and remaining_guesses > 0:
        print("\n" + hangman_stages[6 - remaining_guesses])
        print("Current word:", " ".join(display))
        print("Guessed letters:", ", ".join(sorted(guessed)) if guessed else "None")
        print("Remaining guesses:", remaining_guesses)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        
        guessed.add(guess)
        
        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
        else:
            print("That letter is not in the word.")
            remaining_guesses -= 1
    
    
    print("\n" + hangman_stages[6 - remaining_guesses])
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        print("You win!")
    else:
        print("Sorry, you ran out of guesses. The word was:", word)
        print("Better luck next time!")


while True:
    hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break