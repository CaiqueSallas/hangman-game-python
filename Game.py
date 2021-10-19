from Screen import Screen
from Word import Word


class Game(Word, Screen):
    wins = 0

    def __init__(self):
        self.screen = {
            'content': []
        }
        self.shadow_word = None
        self.tries_letters = set([])
        self.tries = 6
        self.guessed = set([])
        self.winner = False

    def start(self):
        self.refresh_screen()
        input()

        super().__init__()
        self.refresh_screen()

        while self.tries > 0 and len(set(self.word.replace(' ', ''))) != len(self.guessed):
            self.ask_letter()
            self.refresh_screen()

        reset = self.end()

        self.reset() if reset.upper() == 'Y' else 0

    def refresh_screen(self):
        content = [
            self.BODY[self.tries]
        ]

        if self.winner:
            content.extend(['Congratulations!!!', 'Wanna Play Again? Y/N'])
        elif self.tries == 0:
            content.extend(['GAME OVER :(', 'Wanna try Again? Y/N'])
        elif self.shadow_word is not None:
            content.extend([self.shadow_word, 'Guess a letter', 'tries: '
                            + ' '.join(self.tries_letters - self.guessed), 'wins: ' + str(self.wins)])
        else:
            content.append('Type Any Key To Start')

        self.set_screen(content)

    def ask_letter(self):
        letter = ''
        while letter == '':
            letter = input().strip()

        self.tries_letters.add(str(letter[0:1]).upper())
        self.verify_letters()

    def end(self):
        if self.tries == 0:
            self.refresh_screen()
            return input()
        self.winner = True
        self.wins += 1
        self.refresh_screen()
        return input()

    def reset(self):
        self.__init__()
        self.start()


game = Game()
game.start()
