from words import word_list
import random

# welcome the user
name = input("What is you name? ")
print("Ok," + name + ", let's play hangman!")


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play_hangman(word):
    word_completion = "_" * len(word)
    guessed_words = []
    guessed_letters = []
    tries = 6
    guessed = False

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Take your guess: ").upper()

        # if user guesses one letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that, you dufus!")
            elif guess not in word:
                print("Sorry that letter is not in the word. ")
                guessed_letters.append(guess)
                tries -= 1
            else:
                print("You guessed correctly, " + guess + " is part of our word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        # if user guesses a whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word, you dufus! ")
            elif guess != word:
                print("Sorry, " + guess + " is not the hidden word, try again ")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Sorry, that was not a valid guess. ")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

        if guessed:
            print("Congrats you guessed the correct word " + word)
        elif guessed == False and tries <= 0:
            print("Sorry, you ran out of tries")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play_hangman(word)
    while input("Would you like to play again? (Y/N)").upper == "Y":
        word = get_word()
        play_hangman(word)


if __name__ == "__main__":
    main()


