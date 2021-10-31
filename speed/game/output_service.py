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
    
    def print_words(self, words, coords, screen):
        num = 0
        for coord in coords:
            word = screen.print_at(words[num], coord[0], coord[1])
            num += 1

        
        screen.refresh()
        sleep(99999)

    def refrescar(self):
        self.screen.refresh()

    def sleep(self, time):
        sleep(time)

    """def experiment(self):
        with ManagedScreen() as screen:
            centre = (screen.width // 2, screen.height // 2)
            curve_path = []
            for i in range(0, 11):
                curve_path.append(
                    (centre[0] + (screen.width / 4 * math.sin(i * math.pi / 5)),
                    centre[1] - (screen.height / 4 * math.cos(i * math.pi / 5))))
            path = Path()
            path.jump_to(centre[0], centre[1] - screen.height // 4),
            path.move_round_to(curve_path, 60)
            sprite = Sprite(
                screen,
                renderer_dict={
                    "default": StaticRenderer(images=["X"])
                },
                path=path,
                colour=Screen.COLOUR_RED,
                clear=False)"""
#os = OutputService()
#os.print_words("hello world", (1,2))




