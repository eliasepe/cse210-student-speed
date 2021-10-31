from asciimatics.screen import Screen 
from game.director import Director
"""from game.input_service import InputService
from game.output_service import OutputService


def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

Screen.wrapper(main)"""

def main(screen):
    director = Director(screen)
    director.start_game()

Screen.wrapper(main)