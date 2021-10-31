from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep

class OutputService:
    def __init__(self):
        pass
    
    def print_words(self, words, coords):
        with ManagedScreen() as screen:
            self.screen = screen
            num = 0
            for coord in coords:
                screen.print_at(words[num], coord[0], coord[1])
                num += 1
            
            screen.refresh()
            sleep(99999)
            
    def refrescar(self):
        self.screen.refresh()

    def sleep(self, time):
        sleep(time)
            

#os = OutputService()
#os.print_words("hello world", (1,2))




