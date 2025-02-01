import cipher

class Caesar(cipher.Cipher):
    '''
    A Class to represent a Caesar
    -----
    Attributes:
    _shift(int) - User input that choose how many to shift a letter
    '''
    def __init__(self, shift):
        '''Initialize _shift'''
        super().__init__()
        self._shift = shift

    def _encrypt_letter(self, letter):
        '''encrypt a letter by caesar method'''
        self.letter = letter
        index = (self._alphabet.index(self.letter) + self._shift) % 26
        self.letter = self._alphabet[index]
        return self.letter

    def _decrypt_letter(self, letter):
        '''decrypt a letter by caesar method'''
        self.letter = letter
        index = (self._alphabet.index(self.letter) - self._shift) % 26
        self.letter = self._alphabet[index]
        return self.letter


