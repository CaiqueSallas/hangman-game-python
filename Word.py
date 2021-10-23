from random import choice


class Word:
    WORDS = [
        'COMPUTER',
        'MOUSE',
        'KEYBOARD',
        'MOTHERBOARD',
        'MOUSE PAD',
    ]

    def __init__(self):
        self.tries = 6
        self.word = self.generate_word()
        self.shadow_word = self.cover_word()
        self.tries_letters = set([])
        self.guessed = set([])

    def generate_word(self):
        return choice(self.WORDS)

    def cover_word(self):
        return ''.join([' {} '.format(x) if x in self.tries_letters
                        else ' * ' if x == ' '
                        else ' _ ' for x in self.word])

    def verify_letters(self):
        self.tries = 6
        for letter in self.tries_letters:
            if letter not in self.word:
                self.tries -= 1
            else:
                self.guessed.add(letter)
        self.shadow_word = self.cover_word()
