from random import randint

def print_rock_ascii():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')

def print_paper_ascii():
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''')

def print_scissors_ascii():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

def generate_computer_choice():
    ''' Randomly generate an answer for the computer player. '''

    return int(randint(0, 2))

def retrieve_user_choice():
    ''' Get and assign one of three choices from the user. '''

    player_input = ''

    while(1):
        player_input = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n> ')

        try:
            if int(player_input) in (0, 1, 2):
                break
            else:
                print('You must enter a valid choice of 0, 1, or 2.')
        except ValueError:
            print('You must enter a number.')

    return int(player_input)

def print_player_ascii_choices(player_choice, computer_choice):
    ''' Visuals dependent on both player choices. '''

    print('\nYou chose:')

    if player_choice == 0:
        print_rock_ascii()
    elif player_choice == 1:
        print_paper_ascii()
    elif player_choice == 2:
        print_scissors_ascii()

    print('Computer chose:')

    if computer_choice == 0:
        print_rock_ascii()
    elif computer_choice == 1:
        print_paper_ascii()
    elif computer_choice == 2:
        print_scissors_ascii()

def evaluate_winner(player_choice, computer_choice):
    ''' Determines whether the player or computer wins the round. '''

    if player_choice == 0 and computer_choice == 0:
        print('It\'s a draw!\n')
    elif player_choice == 0 and computer_choice == 1:
        print('You lose!\n')
    elif player_choice == 0 and computer_choice == 2:
        print('You win!\n')
    elif player_choice == 1 and computer_choice == 0:
        print('You win!\n')
    elif player_choice == 1 and computer_choice == 1:
        print('It\'s a draw!\n')
    elif player_choice == 1 and computer_choice == 2:
        print('You lose!\n')
    elif player_choice == 2 and computer_choice == 0:
        print('You lose!\n')
    elif player_choice == 2 and computer_choice == 1:
        print('You win!\n')
    elif player_choice == 2 and computer_choice == 2:
        print('It\'s a draw!\n')
    else:
        print('Unknown error occurred!\n')

if __name__ == '__main__':
    player_choice = retrieve_user_choice()
    computer_choice = generate_computer_choice()
    print_player_ascii_choices(player_choice, computer_choice)
    evaluate_winner(player_choice, computer_choice)
