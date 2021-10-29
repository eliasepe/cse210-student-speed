import random
#import os
class Words:
    def __init__(self):
        self.words_list = []
        self.words_on_screen = []

    def importing(self):
        """Import the words.txt file and creates a list with the words in the file"""
        with open("speed\game\words.txt", "rt") as words_file:  #To import you can use the "Path" or the "Relative Path"
            for word in words_file:
                self.words_list.append(word)

    def ran_word(self):
        """return a random word from words list"""
        lista = self.words_list
        word = random.choice(lista)
        return word

    def words_on_screen(self):
        for x in range(1,5):
            word = self.words.ran_word()
            self.words_on_screen.append(word)





#print (os.listdir())
"""xd = Words()
xd.importing()
print (xd.ran_word())"""
