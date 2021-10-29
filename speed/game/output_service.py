from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep

class OutputService:
    def __init__(self):
        pass
    def print_words(self, word, coordi):
        with ManagedScreen() as screen:
            screen.print_at(word, coordi[0], coordi[1])
            screen.refresh()
            sleep(10)

#os = OutputService()
#os.print_words("hello world", (1,2))




