import random
import os
class Words:
    def __init__(self):
        self.words_list = []

    def importing(self):
        """Import the words.txt file and creates a list with the words in the file"""
        with open("words.txt", "rt") as words_file:
            for word in words_file:
                self.words_list.append(word)

    def ran_word(self):
        """return a random word from words list"""
        lista = self.words_list
        word = random.choice(lista)
        return word


"""
print (os.listdir())
xd = Words()
xd.importing()
print (xd.ran_word())"""
