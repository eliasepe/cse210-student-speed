from game.input_service import InputService
from game.output_service import OutputService
from game.player import Player
from game.words import Words
from game.coordinates import Coordinates

"""from input_service import InputService
from output_service import OutputService
from player import Player
from words import Words
from coordinates import Coordinates
"""
class Director:
    def __init__(self):
        self.player = Player()
        self.words = Words()
        self.coordinates = Coordinates()
        self.output = OutputService()

    def start_game(self):
        self.create_board()
        self.words.words_list 

    def create_board(self): 
        self.words.words_on_screen()
        five_words =  self.words.gen_words
        print(five_words)
        for word in five_words:
            coordi = self.coordinates.gen_random()
            print(coordi)
            self.output.print_words(word, coordi)
            #screen.print_at(word, coordi[0], coordi[1])

#dire = Director()
#dire.start_game()