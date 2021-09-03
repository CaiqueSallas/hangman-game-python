import os
import time
import random


def hide_word(word):
    count = word.count(' ')

    shadow_word = ' _ ' * len(word)
    space_position = [None] * count

    for i in range(0, count):
        if i != 0:
            space_position[i] = word.find(' ', space_position[i - 1] + 1)
        else:
            space_position[i] = word.find(' ')

    for position in space_position:
        position = (len(word[:position]) * 3 + 2)
        shadow_word = shadow_word[0:position - 1] + '*' + shadow_word[position:]

    return shadow_word


def boxing(x, y, draw):
    tab = ' ' * 5
    ex = '_' * (x + 5)
    space = ' ' * (x + 5)
    print(' ' + ex)
    count = y - len(draw) - 5
    for l in range(0, y - len(draw) - 5):
        print('|' + space + '|')

    for d in draw:
        stickman = ' ' * (x - len(d))
        print('|' + tab + d + stickman + '|')
    for l in range(0, 5):
        print('|' + space + '|')
    print('|' + ex + '|')


def clear():
    os.system('cls')


def initialize(word):
    tab = ' ' * 4

    for i in range(0, 3):
        boxing(16, 12,
               ['Jogo Da Forca!!!', '  _' * 4, ' 0 ' + tab * 2 + ' |', '/|\\' + tab * 2 + ' |',
                '/ \\' + tab * 2 + ' |'])

        time.sleep(0.5)

        clear()

        time.sleep(0.5)

    shadow_word = hide_word(word)

    boxing(36, 15,
           ['Jogo Da Forca!!!',
            '  _' * 4,
            tab * 2 + '    |',
            tab * 2 + '    |',
            tab * 2 + '    |',
            '',
            '',
            shadow_word])


def sort_word():
    words = [''] * 5
    words[0] = 'Computer'
    words[1] = 'Mouse'
    words[2] = 'Keyboard'
    words[3] = 'Motherboard'
    words[4] = 'Mouse Pad'
    return random.choice(words)


def start():
    word = sort_word()

    initialize(word)

start()
input()
