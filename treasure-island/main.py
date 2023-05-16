def intro():
    ''' Introduction text for the game. '''

    print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
    ''')

    print('Welcome to Treasure island.')
    print('Your mission is to find the treasure.')

def first_choice():
    ''' The player's first choice. '''

    player_input = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n> ')
    check_for_player_loss(choice=1, answer=player_input)

def second_choice():
    ''' The player's second choice. '''

    player_input = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n> ')
    check_for_player_loss(choice=2, answer=player_input)

def third_choice():
    ''' The player's third choice. '''

    player_input = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n> ')
    check_for_player_loss(choice=3, answer=player_input)

def check_for_player_loss(choice, answer):
    ''' Evaluates every choice the player makes to determine if a loss has occurred. Exits the game if so. '''

    if choice == 1 and answer != 'left':
        print('You fell into a hole. Game over!')
        exit()
    
    if choice == 2 and answer != 'wait':
        print('You were attacked by trout. Game over!')
        exit()

    if choice == 3 and answer != 'yellow':
        print('You were burned by fire. Game over!')
        exit()

if __name__ == '__main__':
    intro()
    first_choice()
    second_choice()
    third_choice()

    print('\nYou made it to the Promised Land. You win!\n')
