from game.input_service import InputService
from game.output_service import OutputService
from game.player import Player
from game.words import Words
from game.coordinates import Coordinates

class Director:
    def __init__(self):
        self.player = Player()
        self.words = Words()
        self.coordinates = Coordinates()
        self.output = OutputService()

    def start_game(self):
        self.words.words_list
        self.create_board()

    def create_board(self):  
        for word in self.words.words_on_screen:
            coordi = self.coordinates.gen_random()
            self.output.print_words(word, coordi)
            #screen.print_at(word, coordi[0], coordi[1])

