import random


word_bank = ['Brigham', 'Young', 'University',
             'Aliens', 'Upsidedown', 'Baseball',
             'Georgia', 'Easy', 'Ten', 'Jumbo']
gallows = ["  ,---<\n  |   |\n      |\n      |\n      |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n      |\n      |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n  |   |\n      |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n /|   |\n      |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n /|\  |\n      |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n /|\  |\n /    |\n      |\n<=========>",

        "  ,---<\n  |   |\n  0   |\n /|\  |\n / \  |\n      |\n<=========>"]


def greeting():  # Greet the user welcoming them to the game.
    print('Hello player! Welcome to Hangman.')
    print(gallows[0])
    print('---------------------------------') # used throughout code to provide separation.


def word_select(word):  # Select a random word from the word bank.
    rand_wrd = random.choice(word)
    return rand_wrd


def inform_player(wrd):  # Indicate to the player how many letters are in the word.
    ln_wrd = len(wrd)
    print(f'There are {ln_wrd} letters in the word.')
    print('---------------------------------') 


def letter_guess(wrd, guessed_letters, word_display, wrong_words, counter, right_counter, wrong_counter, player_guess): 
    print('---------------------------------')
    for i in range(len(wrd)): # used to create the word_display.
        if wrd[i].lower() == player_guess.lower():
            word_display[i] = wrd[i].lower()

    if player_guess.lower() in guessed_letters: # used to make sure player does not pick the same letter.
        print('You have already guessed this letter!')
        print(word_display)
        print(f'Your wrong guesses are {wrong_words}')
        print(f'You have guessed {counter} time(s). With {right_counter} right guesses and {wrong_counter} wrong guesses.')

    elif player_guess.lower() in wrd.lower(): # used for correct guess.
        guessed_letters.append(player_guess.lower())
        print('You guessed correctly! ')
        print(word_display)
        print(f'You have guessed {counter} time(s). With {right_counter} right guesses and {wrong_counter} wrong guesses.')

    else: # used for incorrect guess.
        guessed_letters.append(player_guess.lower()) 
        wrong_words.append(player_guess)
        print(f'Sorry, {player_guess} is not in the word.')
        print(word_display)
        print(f'Your wrong guesses are {wrong_words}')
        print(f'You have guessed {counter} time(s). With {right_counter} right guesses and {wrong_counter} wrong guesses.')

    print('---------------------------------')
    return word_display

def game_end(): # used to continue or end the game.
    user_input = input('Would you like to play again? (y/n): ')

    if user_input.lower() in ['y', 'yes']:
        print('|')  # Add some space between games.
        print('|')
        print('|')
        print('|')
        main_play()
    else:
        print('|')
        print('|')
        print('|')
        print('|')
        print('Thank you for playing!')
        exit()


def main_play():  # combine functions into one main gameplay.
    greeting()
    word = word_select(word_bank)
    inform_player(word)
    guessed_letters = []
    word_display = ['-'] * len(word)
    wrong_words = []
    counter = 1
    right_counter = 0  # keep track of the number of correct and incorrect answers.
    wrong_counter = 0
    i = 1  # print the gallows in the proper position.

    while True:
        player_guess = input('Please guess a letter: ') # User is asked to guess a letter.
        if player_guess.lower() not in word.lower():
            print(gallows[i])
            i += 1
            if i >= len(gallows):
                print(f'You took too many guesses. GAME OVER.')
                break
        if player_guess.lower() in word.lower():
            right_counter += 1

        elif player_guess.lower() not in word.lower():
            wrong_counter += 1
        word_display = letter_guess(word, guessed_letters, word_display, wrong_words, counter, right_counter, wrong_counter, player_guess)
        counter += 1

        if set(guessed_letters) == set(word.lower()):
            print(f'Congratulations, you guessed the word! It took you {counter} guesses.')
            break
    game_end()


main_play()












