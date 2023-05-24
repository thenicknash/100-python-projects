import caesar_cipher

def print_roman_soldier():
    print('\n\nWELCOME TO CAESAR CIPHER!\n')
    print('''
              ___       
              \\\\||      
             ,'_,-\\     
             ;'____\\    
             || =\\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \\  \\  |     ',,/,;
      \\  \\ |    /, / ,;
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;
           �-._ `-._,,;
           |/,,`-._ `-.
           |, ,;, ,`-._\\
    \n''')

def set_crypt_choice():
    ''' Determines whether to encrypt or decrypt. '''
    valid_answer = False
    while(valid_answer == False):

        user_choice = input('Type \'encode\' to encrypt, \'decode\' to decrypt:\n> ').lower().strip()
        try:
            cipher.set_crypt_choice(user_choice)
            valid_answer = True
        except:
            print('You must enter a valid response!')

def set_message():
    ''' Gets the message to encrypt or decrypt. '''
    valid_answer = False
    while(valid_answer == False):

        message = input('\nType your message:\n> ').lower().strip()
        try:
            cipher.set_message(message)
            valid_answer = True
        except:
            print('You must enter a valid response!')

def set_shift():
    ''' Gets the number of shifts to perform for each letter. '''
    valid_answer = False
    while(valid_answer == False):

        shift = input('\nType the shift number:\n> ').strip()
        try:
            cipher.set_shift(int(shift))
            valid_answer = True
        except:
            print('You must enter a valid response!')

def print_result():
    ''' Prints the result of the encryption or decryption. '''
    if cipher.crypt_choice == 'encode':
        print(f'\nHere\'s the encoded result: {cipher.encrypt()}')
    else:
        print(f'\nHere\'s the decoded result: {cipher.decrypt()}')

def evaluate_play_again():
    ''' Determines if the user wants to play again. '''
    valid_answer = False
    while(valid_answer == False):

        answer = input('\nType \'yes\' if you want to go again. Otherwise type \'no\':\n> ').lower().strip()

        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('You must enter a valid response!')

if __name__ == '__main__':   
    keep_playing = True

    while keep_playing == True:
        cipher = caesar_cipher.CaesarCipher()

        print_roman_soldier()

        set_crypt_choice()

        set_message()

        set_shift()

        print_result()

        play_again = evaluate_play_again()

        if play_again == False: break