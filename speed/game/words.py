import random
#import os
class Words:
    def __init__(self):
        self.words_list = []
        self.gen_words = []

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
        """choose 5 words to show on the screen"""
        self.importing()
        for x in range(1,5):
            word = self.ran_word()
            self.gen_words.append(word)





#print (os.listdir())
"""xd = Words()
xd.importing()
print (xd.ran_word())"""

