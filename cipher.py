
class Cipher:
    '''
    A Class to represent a Cipher
    -----
    Attributes:
    _alphabet(str) - string of letters in alphabetic order
    '''

    def __init__(self):
        '''Initialize _alphabet'''
        self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt_message(self, message):
        '''make a message in uppercase and encrypt a each letter in the message'''
        self.message = message.upper()
        self.encrypted = ''
        for letter in self.message:
            if letter.isalpha():
                self.encrypted += self._encrypt_letter(letter)
            else:
                self.encrypted += letter
        return self.encrypted
           

    def decrypt_message(self,message):
        '''make a message in uppercase and decrypt a each letter in the message'''
        self.message = message.upper()
        self.decrypted = ''
        for letter in self.message:
            if letter.isalpha():
                self.decrypted += self._decrypt_letter(letter)
            else:
                self.decrypted += letter
        return self.decrypted


    def _encrypt_letter(self,letter):
        '''Encrypt a letter by atbash method'''
        self._reversed_alphabet = self._alphabet[::-1] #slicing

        position = self._alphabet.index(letter)
        return self._reversed_alphabet[position]


    def _decrypt_letter(self,letter):
        '''Decrypt a letter by atbash method'''
        self._reversed_alphabet = self._alphabet[::-1] #slicing

        position = self._reversed_alphabet.index(letter)
        return self._alphabet[position]

