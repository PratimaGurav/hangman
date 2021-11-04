import random
import string
from words import words
from hangman_display import display_hangman


def start_game():
    """
    Function for logo
    """
    print(
        """
         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                            |___/
        """
    )
    # print the welcome message
    name = input("What is your name?\n")
    print(f"Hello, {name}")
    if input("Would you like to play Hangman?(Y)").upper() == "Y":
        select_difficulty = ''
        while True:
            select_difficulty = input("Please enter difficulty level: E - easy, H - hard\n")
            select_difficulty = select_difficulty.upper()
            print("You have chosen: ", select_difficulty)
            break
        if select_difficulty == 'H':    
            num_lives = 5
            return num_lives
            hangman(num_lives)
        else: 
            hangman(num_lives)   
    else:
        print("You need to enter a username to continue...\n")  
        start_game()


# function to get random word from the list
def get_word():
    """Picks a random word from words.py"""
    word = random.choice(words)
    return word.upper()


# function for game
def hangman(num_lives):
    """Play the game"""
    word = get_word()
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = num_lives

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left')
        print('You have used these letters: ', ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(display_hangman[lives])
        print('Guess the word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(display_hangman[lives])
        print('You died, sorry. The word was', word)
        restart_game(num_lives)
    else:
        print('You have guessed the word', word, '\n Congratulations!!')
        restart_game(num_lives)


def restart_game(num_lives):
    """ Gives player an option to restart, otherwise returns to title screen 
    """
    game_restart = False

    while not game_restart:
        restart = input('Would you like to play Hangman again? (Y/N)\n').upper()

        if restart == "Y":
            game_restart = True
            start_game()

        elif restart == "N":
            game_restart = True
            print('Goodbye!')
            start_game()

        else:
            print('You must select Y or N. Please try again.')

def main():
     "main"
     start_game()

main()     