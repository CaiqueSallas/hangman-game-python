from os import system


class Screen:
    def __init__(self, content):
        self.screen = {
            'content': content
        }

    BODY = [
        """ 
           _______________
           |             | 
           0             | 
          /|\\            | 
          / \\            |  
                         |  """,
        """ 
           _______________
           |             | 
           0             | 
          /|\\            | 
          /              |  
                         |  """,
        """ 
           _______________
           |             | 
           0             | 
          /|\\            | 
                         |  
                         |  """,
        """
           _______________
           |             | 
           0             | 
          /|             | 
                         |  
                         |  """,
        """ 
           _______________
           |             | 
           0             | 
           |             | 
                         |  
                         |  """,
        """
           _______________
           |             | 
           0             | 
                         | 
                         |  
                         |  """,
        """
           _______________
           |             | 
                         | 
                         | 
                         |  
                         |  """,
    ]

    @staticmethod
    def clear():
        system('cls')

    def set_screen(self, content):
        self.clear()
        self.screen['content'] = []
        for element in content:
            self.screen['content'].append(element)
        self.display_screen()

    def display_screen(self):
        print('*----------*HANGMAN*----------*' + '\n')
        for i in self.screen['content']:
            print(i + '\n')
