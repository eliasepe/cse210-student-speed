from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

from time import sleep
import math
from asciimatics.paths import Path
class OutputService:
    def __init__(self, screen):
        self.screen = screen
    
    def print_words(self, words, coords, buffer, screen):
        repeat = []
        num = 0
        if len(words) == 0:
            screen.print_at("Congrats! You won the game", 30, 10)
        for word in words:
            #if words[num] not in repeat:
            x = screen.print_at(word, (coords[num])[0], (coords[num])[1])
            if num < len(coords):
                num += 1
                #repeat.append(words[num])
            #elif words[num] in appended:
            #    break
        buffer = screen.print_at(f"Buffer: {buffer}-------------------", 0, 20)
        screen.refresh()

    def reset_buffer(self,screen):
            buffer = screen.print_at(f"Buffer: -------------------", 0, 20)
            screen.refresh()

        

    def clean(self,screen):
        screen.clear()

    def sleep(self, time):
        sleep(time)

   
#os = OutputService()
#os.print_words("hello world", (1,2))




