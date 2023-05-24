class CaesarCipher:
    def __init__(self):
        self.alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    def set_crypt_choice(self, user_choice):
        ''' Sets the user's choice whether to encrypt or decrypt the text. '''
        if user_choice not in ['encode', 'decode']: raise Exception()
        self.crypt_choice = user_choice

    def set_shift(self, number):
        ''' Sets the number of shifts to perform for each letter. '''
        if number < 0: raise Exception()
        self.shift = number

    def set_message(self, message):
        ''' Sets the message to encrypt or decrypt. '''
        if not message.isalpha(): raise Exception()
        self.message = message

    def encrypt(self):
        ''' Encrypts the set message. '''
        message_letters = list(self.message)
        encoded_message_letters = []

        for index, letter in enumerate(message_letters):
            index = self.alphabet.index(letter)
            shifted_index = index + self.shift

            if shifted_index >= len(self.alphabet):
                shifted_index = shifted_index - len(self.alphabet)

            encoded_message_letters.append(self.alphabet[shifted_index])

        return ''.join(encoded_message_letters)

    def decrypt(self):
        ''' Decrypts the set message. '''
        message_letters = list(self.message)
        encoded_message_letters = []

        for index, letter in enumerate(message_letters):
            index = self.alphabet.index(letter)
            shifted_index = index - self.shift

            if shifted_index < 0:
                shifted_index = len(self.alphabet) + shifted_index

            encoded_message_letters.append(self.alphabet[shifted_index])

        return ''.join(encoded_message_letters)
