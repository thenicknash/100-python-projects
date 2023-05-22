import random
import requests

def print_intro():
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
    ''')

def generate_random_word():
    ''' Generates a random word for the player to guess by making an API call to MIT word file. '''
    random_words_url = 'https://www.mit.edu/~ecprice/wordlist.10000'
    response = requests.get(random_words_url)
    content_string = str(response.content, 'utf-8')
    words = content_string.splitlines()
    return random.choice(words)

def generate_random_word_letters(word: str):
    ''' Creating the list of underscores to match the random word length. '''
    missing_letters = []

    for letter in range(1, len(word) + 1):
        missing_letters.append('_')

    return missing_letters

def get_player_guess():
    ''' Retrieves the players guess. Meant to be called until game ends. '''
    guess = input('\nGuess a letter: ').lower()

    # TODO: Add letter validation here

    return guess

def evaluate_player_guess(guessed_letter, random_word, random_word_letters):
    ''' Checks to see if guessed letter is in the word. '''
    updated_random_word_letters = random_word_letters
    correct_guess = False

    for index, letter in enumerate(random_word):
        if guessed_letter == letter:
            updated_random_word_letters[index] = guessed_letter
            correct_guess = True

    return {
        'updated_random_word_letters': updated_random_word_letters,
        'correct_guess': correct_guess
    }

def evaluate_player_wins(random_word_letters):
    ''' Checks to see if all of the letters have been correctly guessed. '''
    if '_' not in random_word_letters:
        return True


if __name__ == '__main__':
    RANDOM_WORD = generate_random_word()
    N_LETTERS_IN_RANDOM_WORD = list(RANDOM_WORD)
    MAX_NUMBER_OF_LIVES = len(N_LETTERS_IN_RANDOM_WORD) + 3
    n_lives_left = MAX_NUMBER_OF_LIVES
    random_word_letters = generate_random_word_letters(RANDOM_WORD)
    letters_guessed = []

    print_intro()

    while n_lives_left > 0:
        guess = get_player_guess()
        letters_guessed.append(guess)
        letters_guessed_display = ', '.join(letters_guessed)

        player_guess_evaluation = evaluate_player_guess(guess, RANDOM_WORD, random_word_letters)

        random_word_letters = player_guess_evaluation['updated_random_word_letters']

        if player_guess_evaluation['correct_guess'] == False:
            n_lives_left -= 1

        player_wins = evaluate_player_wins(random_word_letters)
        if player_wins == True:
            print(f'\nTHE WORD: {RANDOM_WORD}')
            print('\nCongratulations! You won!\n')
            break

        if n_lives_left == 0:
            print(f'\nTHE WORD: {RANDOM_WORD}')
            print('\nYou ran out of guesses. You lose!\n')
            break

        print(f'\n{n_lives_left} lives left!')
        print(f'\nLetters guessed: [ {letters_guessed_display} ]\n')
        print(' '.join(random_word_letters))
