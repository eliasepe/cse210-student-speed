from game.input_service import InputService
from game.output_service import OutputService
from game.player import Player
from game.words import Words
from game.coordinates import Coordinates

class Director:
    def __init__(self, screen):
        self.player = Player()
        self.words = Words()
        self.coordinates = Coordinates()
        self.output = OutputService(screen)
        self.screen = screen

    def start_game(self):
        self.create_board()


    def create_board(self): 
        self.words.words_on_screen()
        five_words =  self.words.gen_words
        #print(five_words)
        buffer = ""
        while True:
            coord1 = self.coordinates.gen_random()
            coord2 = self.coordinates.gen_random()
            coord3 = self.coordinates.gen_random()
            coord4 = self.coordinates.gen_random()
            coord5 = self.coordinates.gen_random()

            coords = [coord1, coord2, coord3, coord4, coord5]
        
            
            #self.output.reset_buffer(self.screen)
            buffer = input("Type the word: ")  
            if buffer in five_words:
                five_words.remove(buffer)
                coords.pop(0)
                
            self.output.print_words(five_words, coords,buffer, self.screen)      
            self.output.sleep(2)
            self.output.clean(self.screen)
            


        
            #screen.print_at(word, coordi[0], coordi[1])

#dire = Director()
#dire.start_game()